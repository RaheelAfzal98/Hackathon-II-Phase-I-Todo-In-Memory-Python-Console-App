"""Todo data models for the in-memory CLI application."""

from dataclasses import dataclass
from typing import Optional, List
from uuid import uuid4
from datetime import datetime, timedelta


@dataclass
class Todo:
    """Represents a single todo item."""

    id: str
    title: str
    description: str
    completed: bool = False
    priority: str = "medium"  # "high", "medium", "low"
    tags: List[str] = None  # List of tags
    due_date: Optional[datetime] = None  # Optional due date and time for the task
    is_recurring: bool = False  # Flag indicating if the task recurs
    recurrence_pattern: Optional[str] = None  # Pattern for recurrence (daily, weekly, custom)
    recurrence_interval: Optional[int] = None  # Interval in days for custom recurrence patterns

    def __post_init__(self):
        """Initialize default values after dataclass initialization."""
        if self.tags is None:
            self.tags = []
        if self.priority not in ["high", "medium", "low"]:
            self.priority = "medium"
        # Validate recurrence fields
        if self.is_recurring and self.recurrence_pattern is None:
            self.recurrence_pattern = "daily"  # Default to daily if recurring but no pattern specified
        if self.recurrence_pattern is not None and self.recurrence_pattern not in ["daily", "weekly", "custom"]:
            self.recurrence_pattern = "daily"  # Default to daily if invalid pattern
        if self.recurrence_pattern == "custom" and (self.recurrence_interval is None or self.recurrence_interval <= 0):
            self.recurrence_interval = 1  # Default to 1 day if custom pattern but no valid interval
        if self.recurrence_pattern != "custom":
            self.recurrence_interval = None  # Clear interval if not custom pattern


class TodoModel:
    """Data model for managing todo items in memory."""

    def __init__(self):
        """Initialize an empty collection of todos."""
        self.todos = {}

    def add_todo(self, title: str, description: str = "", priority: str = "medium", tags: List[str] = None,
                 due_date: Optional[datetime] = None, is_recurring: bool = False,
                 recurrence_pattern: Optional[str] = None, recurrence_interval: Optional[int] = None) -> Todo:
        """Add a new todo item to the collection."""
        todo_id = str(uuid4())
        todo = Todo(
            id=todo_id,
            title=title,
            description=description,
            completed=False,
            priority=priority,
            tags=tags if tags is not None else [],
            due_date=due_date,
            is_recurring=is_recurring,
            recurrence_pattern=recurrence_pattern,
            recurrence_interval=recurrence_interval
        )
        self.todos[todo_id] = todo
        return todo

    def get_all_todos(self) -> list[Todo]:
        """Retrieve all todo items."""
        return list(self.todos.values())

    def get_todo(self, todo_id: str) -> Optional[Todo]:
        """Retrieve a specific todo item by ID.

        Supports both full UUID and partial ID matching.
        """
        # First try exact match
        if todo_id in self.todos:
            return self.todos[todo_id]

        # If no exact match, try partial ID matching
        matches = [todo for id, todo in self.todos.items() if id.startswith(todo_id)]

        if len(matches) == 1:
            return matches[0]
        elif len(matches) > 1:
            # Multiple matches found for partial ID
            return None
        else:
            # No matches found
            return None

    def update_todo(self, todo_id: str, title: str = None, description: str = None, priority: str = None, tags: List[str] = None,
                    due_date: Optional[datetime] = None, is_recurring: bool = None,
                    recurrence_pattern: Optional[str] = None, recurrence_interval: Optional[int] = None) -> Optional[Todo]:
        """Update an existing todo item."""
        todo = self.get_todo(todo_id)
        if todo is None:
            return None

        if title is not None and title != "":
            todo.title = title
        if description is not None and description != "":
            todo.description = description
        if priority is not None and priority in ["high", "medium", "low"]:
            todo.priority = priority
        if tags is not None:
            todo.tags = tags
        if due_date is not None:
            todo.due_date = due_date
        if is_recurring is not None:
            todo.is_recurring = is_recurring
        if recurrence_pattern is not None:
            todo.recurrence_pattern = recurrence_pattern
            # Validate recurrence pattern
            if recurrence_pattern not in ["daily", "weekly", "custom"]:
                raise ValueError("Recurrence pattern must be one of: daily, weekly, custom")
        if recurrence_interval is not None:
            todo.recurrence_interval = recurrence_interval
            # Validate recurrence interval
            if todo.recurrence_pattern == "custom" and (recurrence_interval is None or recurrence_interval <= 0):
                raise ValueError("Recurrence interval must be a positive integer for custom patterns")

        # Additional validation: if is_recurring is True, recurrence_pattern must be specified
        if todo.is_recurring and todo.recurrence_pattern is None:
            todo.recurrence_pattern = "daily"

        return todo

    def delete_todo(self, todo_id: str) -> bool:
        """Delete a todo item by ID."""
        todo = self.get_todo(todo_id)
        if todo is not None:
            # Find the exact key and delete it
            for key in list(self.todos.keys()):
                if self.todos[key] == todo and (key == todo.id or key.startswith(todo_id)):
                    del self.todos[key]
                    return True
        return False

    def toggle_completion(self, todo_id: str) -> Optional[Todo]:
        """Toggle the completion status of a todo item."""
        todo = self.get_todo(todo_id)
        if todo is None:
            return None

        # If the task is recurring and being marked as complete, generate the next occurrence
        if todo.is_recurring and not todo.completed:
            # Mark current task as complete
            todo.completed = True

            # Generate next occurrence
            next_todo = self.generate_next_occurrence(todo)
            if next_todo:
                self.todos[next_todo.id] = next_todo

            return todo
        else:
            # For non-recurring tasks or unmarking as complete, just toggle the status
            todo.completed = not todo.completed
            return todo

    def generate_next_occurrence(self, todo: Todo) -> Optional[Todo]:
        """Creates the next occurrence of a recurring task."""
        if not todo.is_recurring:
            return None

        # Calculate the next due date based on the recurrence pattern
        next_due_date = None
        if todo.due_date:
            if todo.recurrence_pattern == "daily":
                next_due_date = todo.due_date + timedelta(days=1)
            elif todo.recurrence_pattern == "weekly":
                next_due_date = todo.due_date + timedelta(days=7)
            elif todo.recurrence_pattern == "custom" and todo.recurrence_interval:
                next_due_date = todo.due_date + timedelta(days=todo.recurrence_interval)
            else:
                # If no valid pattern, don't set a due date for the next occurrence
                next_due_date = todo.due_date

        # Create a new todo with the same properties but a new ID and reset completion status
        new_todo = Todo(
            id=str(uuid4()),
            title=todo.title,
            description=todo.description,
            completed=False,  # New occurrence starts as incomplete
            priority=todo.priority,
            tags=todo.tags.copy(),  # Copy the tags
            due_date=next_due_date,
            is_recurring=todo.is_recurring,
            recurrence_pattern=todo.recurrence_pattern,
            recurrence_interval=todo.recurrence_interval
        )

        return new_todo

    def handle_overdue_recurring_task(self, todo_id: str) -> Optional[Todo]:
        """Handle completion of an overdue recurring task to ensure next occurrence is scheduled from current date."""
        todo = self.get_todo(todo_id)
        if todo is None or not todo.is_recurring or not self.is_overdue(todo):
            return None

        # Mark current task as complete
        todo.completed = True

        # Generate next occurrence based on current date instead of original due date
        next_todo = self.generate_next_occurrence_from_current_date(todo)
        if next_todo:
            self.todos[next_todo.id] = next_todo

        return todo

    def generate_next_occurrence_from_current_date(self, todo: Todo) -> Optional[Todo]:
        """Creates the next occurrence of a recurring task based on the current date."""
        if not todo.is_recurring:
            return None

        # Calculate the next due date based on the current date
        next_due_date = None
        current_date = datetime.now()
        if todo.due_date:  # If the original had a due date, calculate from current date
            if todo.recurrence_pattern == "daily":
                next_due_date = current_date + timedelta(days=1)
            elif todo.recurrence_pattern == "weekly":
                next_due_date = current_date + timedelta(days=7)
            elif todo.recurrence_pattern == "custom" and todo.recurrence_interval:
                next_due_date = current_date + timedelta(days=todo.recurrence_interval)
            else:
                # If no valid pattern, don't set a due date for the next occurrence
                next_due_date = current_date

        # Create a new todo with the same properties but a new ID and reset completion status
        new_todo = Todo(
            id=str(uuid4()),
            title=todo.title,
            description=todo.description,
            completed=False,  # New occurrence starts as incomplete
            priority=todo.priority,
            tags=todo.tags.copy(),  # Copy the tags
            due_date=next_due_date,
            is_recurring=todo.is_recurring,
            recurrence_pattern=todo.recurrence_pattern,
            recurrence_interval=todo.recurrence_interval
        )

        return new_todo

    def is_overdue(self, todo: Todo) -> bool:
        """Check if a task is overdue."""
        if todo.due_date is None or todo.completed:
            return False
        return datetime.now() > todo.due_date

    def get_overdue_todos(self) -> List[Todo]:
        """Get all overdue tasks."""
        all_todos = self.get_all_todos()
        overdue_todos = []
        for todo in all_todos:
            if self.is_overdue(todo):
                overdue_todos.append(todo)
        return overdue_todos