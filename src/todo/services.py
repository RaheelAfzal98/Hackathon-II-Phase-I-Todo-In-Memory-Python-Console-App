"""Business logic services for the todo application."""

from typing import List, Optional
from .models import TodoModel, Todo


class TodoService:
    """Service layer for todo operations."""

    def __init__(self):
        """Initialize the todo service with a data model."""
        self.model = TodoModel()

    def add_task(self, title: str, description: str = "", priority: str = "medium", tags: List[str] = None,
                 due_date=None, is_recurring: bool = False, recurrence_pattern: str = None, recurrence_interval: int = None) -> Todo:
        """Add a new task to the todo list."""
        if not title:
            raise ValueError("Title is required")
        if priority not in ["high", "medium", "low"]:
            raise ValueError("Priority must be one of: high, medium, low")
        if is_recurring and recurrence_pattern not in ["daily", "weekly", "custom"]:
            raise ValueError("Recurrence pattern must be one of: daily, weekly, custom")
        if is_recurring and recurrence_pattern == "custom" and (recurrence_interval is None or recurrence_interval <= 0):
            raise ValueError("Recurrence interval must be a positive integer for custom patterns")

        return self.model.add_todo(title, description, priority, tags, due_date, is_recurring, recurrence_pattern, recurrence_interval)

    def list_tasks(self) -> List[Todo]:
        """Get all tasks from the todo list."""
        return self.model.get_all_todos()

    def get_task(self, task_id: str) -> Optional[Todo]:
        """Get a specific task by ID."""
        return self.model.get_todo(task_id)

    def update_task(self, task_id: str, title: str = None, description: str = None, priority: str = None, tags: List[str] = None,
                    due_date=None, is_recurring: bool = None, recurrence_pattern: str = None, recurrence_interval: int = None) -> Optional[Todo]:
        """Update an existing task."""
        if title is not None and not title:
            raise ValueError("Title cannot be empty")
        if priority is not None and priority not in ["high", "medium", "low"]:
            raise ValueError("Priority must be one of: high, medium, low")
        if is_recurring and recurrence_pattern not in ["daily", "weekly", "custom"]:
            raise ValueError("Recurrence pattern must be one of: daily, weekly, custom")
        if is_recurring and recurrence_pattern == "custom" and (recurrence_interval is None or recurrence_interval <= 0):
            raise ValueError("Recurrence interval must be a positive integer for custom patterns")

        return self.model.update_todo(task_id, title, description, priority, tags, due_date, is_recurring, recurrence_pattern, recurrence_interval)

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

    def search_tasks(self, keyword: str, case_sensitive: bool = False) -> List[Todo]:
        """Search tasks by keyword in title, description, or tags."""
        if not keyword:
            return []

        if not case_sensitive:
            keyword = keyword.lower()

        results = []
        for task in self.model.get_all_todos():
            title = task.title if case_sensitive else task.title.lower()
            description = task.description if case_sensitive else task.description.lower()
            # Convert tags to lowercase if not case sensitive
            tags = [tag if case_sensitive else tag.lower() for tag in task.tags]

            # Check if keyword is in title, description, or any of the tags
            if keyword in title or keyword in description or keyword in tags:
                results.append(task)

        return results

    def filter_by_status(self, status: str) -> List[Todo]:
        """Filter tasks by completion status."""
        if status not in ["completed", "incomplete", None]:
            raise ValueError("Status must be one of: completed, incomplete, or None")

        results = []
        for task in self.model.get_all_todos():
            if status == "completed" and task.completed:
                results.append(task)
            elif status == "incomplete" and not task.completed:
                results.append(task)
            elif status is None:
                results.append(task)

        return results

    def filter_by_priority(self, priority: str) -> List[Todo]:
        """Filter tasks by priority level."""
        if priority not in ["high", "medium", "low", None]:
            raise ValueError("Priority must be one of: high, medium, low, or None")

        if priority is None:
            return self.model.get_all_todos()

        return [task for task in self.model.get_all_todos() if task.priority == priority]

    def filter_by_tag(self, tag: str) -> List[Todo]:
        """Filter tasks by specific tag."""
        if not tag:
            return []

        return [task for task in self.model.get_all_todos() if tag in task.tags]

    def combine_filters(self, status: str = None, priority: str = None, tag: str = None) -> List[Todo]:
        """Combine multiple filters."""
        # Start with all tasks
        tasks = self.model.get_all_todos()

        # Apply status filter
        if status is not None:
            if status == "completed":
                tasks = [task for task in tasks if task.completed]
            elif status == "incomplete":
                tasks = [task for task in tasks if not task.completed]

        # Apply priority filter
        if priority is not None:
            tasks = [task for task in tasks if task.priority == priority]

        # Apply tag filter
        if tag is not None:
            tasks = [task for task in tasks if tag in task.tags]

        return tasks

    def sort_tasks(self, tasks: List[Todo], by: str, ascending: bool = True) -> List[Todo]:
        """Sort tasks by specified field."""
        if by not in ["priority", "title", "id"]:
            raise ValueError("Sort field must be one of: priority, title, id")

        if by == "priority":
            # Define priority order: high, medium, low
            priority_order = {"high": 0, "medium": 1, "low": 2}
            # For priority, ascending=False means high priority first
            # ascending=True means low priority first
            # When ascending=False, we don't want to reverse priority order (high first)
            # When ascending=True, we want to reverse priority order (low first)
            sorted_tasks = sorted(tasks, key=lambda x: priority_order[x.priority], reverse=ascending)
        elif by == "title":
            sorted_tasks = sorted(tasks, key=lambda x: x.title.lower(), reverse=not ascending)
        elif by == "id":
            sorted_tasks = sorted(tasks, key=lambda x: x.id, reverse=not ascending)

        return sorted_tasks

    def is_overdue(self, task: Todo) -> bool:
        """Check if a task is overdue."""
        return self.model.is_overdue(task)

    def get_overdue_tasks(self) -> List[Todo]:
        """Get all overdue tasks."""
        return self.model.get_overdue_todos()

    def handle_overdue_recurring_task(self, task_id: str) -> Optional[Todo]:
        """Handle completion of an overdue recurring task."""
        return self.model.handle_overdue_recurring_task(task_id)