"""Business logic services for the todo application."""

from typing import List, Optional
from .models import TodoModel, Todo


class TodoService:
    """Service layer for todo operations."""

    def __init__(self):
        """Initialize the todo service with a data model."""
        self.model = TodoModel()

    def add_task(self, title: str, description: str) -> Todo:
        """Add a new task to the todo list."""
        if not title:
            raise ValueError("Title is required")
        return self.model.add_todo(title, description)

    def list_tasks(self) -> List[Todo]:
        """Get all tasks from the todo list."""
        return self.model.get_all_todos()

    def get_task(self, task_id: str) -> Optional[Todo]:
        """Get a specific task by ID."""
        return self.model.get_todo(task_id)

    def update_task(self, task_id: str, title: str = None, description: str = None) -> Optional[Todo]:
        """Update an existing task."""
        if title is not None and not title:
            raise ValueError("Title cannot be empty")
        return self.model.update_todo(task_id, title, description)

    def delete_task(self, task_id: str) -> bool:
        """Delete a task by ID."""
        return self.model.delete_todo(task_id)

    def mark_task_complete(self, task_id: str) -> Optional[Todo]:
        """Mark a task as complete."""
        return self.model.toggle_completion(task_id)

    def mark_task_incomplete(self, task_id: str) -> Optional[Todo]:
        """Mark a task as incomplete."""
        # Ensure the task exists and is completed before toggling
        task = self.model.get_todo(task_id)
        if task is None:
            return None
        if not task.completed:
            return task  # Already incomplete
        return self.model.toggle_completion(task_id)

    def toggle_task_completion(self, task_id: str) -> Optional[Todo]:
        """Toggle the completion status of a task."""
        return self.model.toggle_completion(task_id)