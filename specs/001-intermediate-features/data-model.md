# Data Model: Intermediate Level Features for Phase I CLI Todo App

**Feature**: Intermediate Level Features (Priorities & Tags, Search & Filter, Sort Tasks)
**Date**: 2026-01-02
**Branch**: 001-intermediate-features

## Entity: TodoItem

### Fields

- **id**: str - Unique identifier for the task (auto-generated)
- **title**: str - Title of the task (required)
- **description**: str - Detailed description of the task (optional, default: "")
- **completed**: bool - Completion status of the task (default: False)
- **priority**: str - Priority level of the task (values: "high", "medium", "low"; default: "medium")
- **tags**: list[str] - List of tags associated with the task (default: [])

### Validation Rules

- **id**: Must be a unique string (UUID format recommended)
- **title**: Must be a non-empty string with length between 1-200 characters
- **description**: Optional, but if provided must be between 0-1000 characters
- **completed**: Must be a boolean value
- **priority**: Must be one of the allowed values: "high", "medium", "low"
- **tags**: Must be a list of strings where each tag is 1-50 characters and contains only alphanumeric characters and hyphens

### State Transitions

- **Creation**: A TodoItem is created with a title, optional description, completed=False, priority="medium", tags=[]
- **Update**: Any field except id can be updated via update operations
- **Deletion**: TodoItem is removed from the collection (no state transition, just removal)

## Entity: TaskCollection

### Fields

- **tasks**: list[TodoItem] - Collection of all TodoItem objects
- **next_id**: int - Counter for generating unique IDs (internal use)

### Validation Rules

- **tasks**: Must be a list of valid TodoItem objects
- **next_id**: Must be a positive integer used for generating unique IDs

### Operations

- **add_task**: Adds a new TodoItem to the collection
- **get_task**: Retrieves a TodoItem by ID
- **update_task**: Updates fields of an existing TodoItem
- **delete_task**: Removes a TodoItem from the collection
- **search_tasks**: Returns subset of tasks matching search criteria
- **filter_tasks**: Returns subset of tasks matching filter criteria
- **sort_tasks**: Returns tasks sorted according to specified criteria

## Entity: SearchQuery

### Fields

- **keyword**: str - Search term to match against title and description
- **case_sensitive**: bool - Whether search should be case-sensitive (default: False)

### Validation Rules

- **keyword**: Must be a non-empty string
- **case_sensitive**: Must be a boolean value

## Entity: FilterCriteria

### Fields

- **status**: str or None - Filter by completion status ("completed", "incomplete", None for all)
- **priority**: str or None - Filter by priority level ("high", "medium", "low", None for all)
- **tag**: str or None - Filter by specific tag (None for all)

### Validation Rules

- **status**: Must be one of the allowed values or None
- **priority**: Must be one of the allowed priority values or None
- **tag**: If provided, must be a valid tag string (1-50 alphanumeric characters and hyphens)

## Entity: SortCriteria

### Fields

- **by**: str - Field to sort by ("priority", "title", "id")
- **ascending**: bool - Sort direction (True for ascending, False for descending)

### Validation Rules

- **by**: Must be one of the allowed sort fields
- **ascending**: Must be a boolean value

## Relationships

- **TaskCollection** contains 0 to N **TodoItem** objects
- **TodoItem** can have 0 to N **tags** (each tag is a string)