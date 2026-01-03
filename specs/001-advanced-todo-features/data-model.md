# Data Model: Advanced Todo Features

## Entity: Todo (Enhanced)

### Fields
- `id: str` - Unique identifier (UUID string) - Primary Key
- `title: str` - Task title (required)
- `description: str` - Task description (optional, default: "")
- `completed: bool` - Completion status (default: False)
- `priority: str` - Priority level (values: "high", "medium", "low", default: "medium")
- `tags: List[str]` - List of tags for categorization (default: [])
- `due_date: Optional[datetime]` - Optional due date and time for the task
- `is_recurring: bool` - Flag indicating if the task recurs (default: False)
- `recurrence_pattern: Optional[str]` - Pattern for recurrence (values: "daily", "weekly", "custom", null)
- `recurrence_interval: Optional[int]` - Interval in days for custom recurrence patterns (null if not custom pattern)

### Relationships
- None (standalone entity)

### Validation Rules
- `title` must not be empty
- `priority` must be one of "high", "medium", "low"
- `recurrence_pattern` must be null when `is_recurring` is False
- `recurrence_pattern` must be one of "daily", "weekly", "custom" when `is_recurring` is True
- `recurrence_interval` must be a positive integer when `recurrence_pattern` is "custom"
- `due_date` must be a valid datetime object or None

### State Transitions
- Normal task: Created → Updated → Completed/Deleted
- Recurring task: Created → Completed → New occurrence created → Updated → Completed → New occurrence created...

## Entity: TodoModel (Collection Manager)

### Responsibilities
- Manages in-memory collection of Todo items
- Provides CRUD operations for Todo items
- Handles recurring task generation logic
- Maintains data integrity and validation

### Methods
- `add_todo(title: str, description: str, priority: str, tags: List[str], due_date: Optional[datetime], is_recurring: bool, recurrence_pattern: Optional[str], recurrence_interval: Optional[int]) -> Todo`
- `get_all_todos() -> List[Todo]`
- `get_todo(todo_id: str) -> Optional[Todo]`
- `update_todo(todo_id: str, title: str, description: str, priority: str, tags: List[str], due_date: Optional[datetime], is_recurring: bool, recurrence_pattern: Optional[str], recurrence_interval: Optional[int]) -> Optional[Todo]`
- `delete_todo(todo_id: str) -> bool`
- `toggle_completion(todo_id: str) -> Optional[Todo]`
- `generate_next_occurrence(todo: Todo) -> Todo` - Creates the next occurrence of a recurring task

## Entity: TaskReminder (Conceptual)

### Responsibilities
- Check if tasks are overdue
- Determine if time-based notifications should be triggered
- Provide status information for CLI display

### Methods
- `is_overdue(task: Todo) -> bool` - Checks if a task is overdue
- `get_overdue_tasks(tasks: List[Todo]) -> List[Todo]` - Returns all overdue tasks
- `is_due_soon(task: Todo, hours: int) -> bool` - Checks if task is due within specified hours