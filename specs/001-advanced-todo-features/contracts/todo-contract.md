# Todo Service Contract: Advanced Features

## Overview
This contract defines the API for the enhanced Todo service with advanced features including recurring tasks and due dates.

## Core Operations

### Create Task with Advanced Options
- **Method**: `add_task(title: str, description: str, priority: str, tags: List[str], due_date: Optional[datetime], is_recurring: bool, recurrence_pattern: Optional[str], recurrence_interval: Optional[int]) -> Todo`
- **Purpose**: Create a new task with optional advanced features
- **Preconditions**:
  - title is not empty
  - priority is one of "high", "medium", "low"
  - if is_recurring is True, recurrence_pattern must be specified
- **Postconditions**: New task exists in the system
- **Return**: Created Todo object with assigned ID

### Get Task with Advanced Fields
- **Method**: `get_task(task_id: str) -> Optional[Todo]`
- **Purpose**: Retrieve a task by ID, including advanced fields
- **Preconditions**: task exists in system
- **Postconditions**: Returns complete task data
- **Return**: Todo object or None if not found

### Update Task with Advanced Options
- **Method**: `update_task(task_id: str, title: str, description: str, priority: str, tags: List[str], due_date: Optional[datetime], is_recurring: bool, recurrence_pattern: Optional[str], recurrence_interval: Optional[int]) -> Optional[Todo]`
- **Purpose**: Update an existing task with advanced features
- **Preconditions**: task exists in system
- **Postconditions**: Task is updated with new values
- **Return**: Updated Todo object or None if not found

### Complete Task with Recurrence Handling
- **Method**: `toggle_task_completion(task_id: str) -> Optional[Todo]`
- **Purpose**: Toggle completion status and handle recurring tasks
- **Preconditions**: task exists in system
- **Postconditions**:
  - If recurring: original task marked complete, new occurrence created
  - If not recurring: task completion status toggled
- **Return**: Updated Todo object or None if not found

### List Tasks with Due Date and Recurrence Filtering
- **Method**: `list_tasks(filter_status: Optional[str], filter_priority: Optional[str], filter_tag: Optional[str], filter_overdue: bool, filter_recurring: bool) -> List[Todo]`
- **Purpose**: Retrieve tasks with optional advanced filters
- **Preconditions**: None
- **Postconditions**: Returns filtered list of tasks
- **Return**: List of Todo objects

### Search Tasks with Advanced Fields
- **Method**: `search_tasks(keyword: str, include_due_date: bool, include_recurrence: bool) -> List[Todo]`
- **Purpose**: Search tasks including advanced fields
- **Preconditions**: None
- **Postconditions**: Returns matching tasks
- **Return**: List of Todo objects

## Advanced Feature Operations

### Generate Next Occurrence
- **Method**: `generate_next_occurrence(task: Todo) -> Todo`
- **Purpose**: Create the next occurrence of a recurring task
- **Preconditions**: Task is a recurring task
- **Postconditions**: New occurrence created with appropriate due date
- **Return**: New Todo object representing next occurrence

### Check Overdue Status
- **Method**: `is_overdue(task: Todo) -> bool`
- **Purpose**: Determine if a task is overdue
- **Preconditions**: Task has a due date
- **Postconditions**: Returns overdue status
- **Return**: Boolean indicating overdue status

### Get Overdue Tasks
- **Method**: `get_overdue_tasks() -> List[Todo]`
- **Purpose**: Retrieve all overdue tasks
- **Preconditions**: None
- **Postconditions**: Returns list of overdue tasks
- **Return**: List of Todo objects