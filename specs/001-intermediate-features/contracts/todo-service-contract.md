# API Contract: Todo Service Interface

## Service: TodoService

### Method: create_task
- **Input**: title: str, description: str = "", priority: str = "medium", tags: list[str] = []
- **Output**: TodoItem
- **Errors**: ValidationError if inputs don't meet validation criteria

### Method: search_tasks
- **Input**: keyword: str, case_sensitive: bool = False
- **Output**: list[TodoItem]
- **Behavior**: Returns tasks where keyword matches title or description

### Method: filter_tasks
- **Input**: status: str = None, priority: str = None, tag: str = None
- **Output**: list[TodoItem]
- **Behavior**: Returns tasks matching all specified filter criteria

### Method: sort_tasks
- **Input**: tasks: list[TodoItem], by: str, ascending: bool = True
- **Output**: list[TodoItem]
- **Behavior**: Returns sorted copy of tasks without modifying original list

### Method: update_task
- **Input**: task_id: str, title: str = None, description: str = None, priority: str = None, tags: list[str] = None, completed: bool = None
- **Output**: TodoItem
- **Errors**: TaskNotFound if task_id doesn't exist