"""Todo data models for the in-memory CLI application."""

from dataclasses import dataclass
from typing import Optional
from uuid import uuid4


@dataclass
class Todo:
    """Represents a single todo item."""

    id: str
    title: str
    description: str
    completed: bool = False


class TodoModel:
    """Data model for managing todo items in memory."""

    def __init__(self):
        """Initialize an empty collection of todos."""
        self.todos = {}

    def add_todo(self, title: str, description: str) -> Todo:
        """Add a new todo item to the collection."""
        todo_id = str(uuid4())
        todo = Todo(
            id=todo_id,
            title=title,
            description=description,
            completed=False
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

    def update_todo(self, todo_id: str, title: str = None, description: str = None) -> Optional[Todo]:
        """Update an existing todo item."""
        todo = self.get_todo(todo_id)
        if todo is None:
            return None

        if title is not None and title != "":
            todo.title = title
        if description is not None and description != "":
            todo.description = description

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

        todo.completed = not todo.completed
        return todo