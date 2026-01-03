#!/usr/bin/env python3
"""Unit tests for TodoItem model with new priority and tags fields."""

import unittest
from src.todo.models import Todo, TodoModel


class TestTodoModel(unittest.TestCase):
    """Test cases for Todo model with priority and tags functionality."""

    def test_todo_creation_with_priority_and_tags(self):
        """Test creating a Todo item with priority and tags."""
        todo = Todo(
            id="test-id",
            title="Test Task",
            description="Test Description",
            completed=False,
            priority="high",
            tags=["work", "urgent"]
        )

        self.assertEqual(todo.id, "test-id")
        self.assertEqual(todo.title, "Test Task")
        self.assertEqual(todo.description, "Test Description")
        self.assertEqual(todo.completed, False)
        self.assertEqual(todo.priority, "high")
        self.assertEqual(todo.tags, ["work", "urgent"])

    def test_todo_creation_with_default_values(self):
        """Test creating a Todo item with default values."""
        todo = Todo(
            id="test-id",
            title="Test Task",
            description="Test Description"
        )

        self.assertEqual(todo.priority, "medium")  # Default priority
        self.assertEqual(todo.tags, [])  # Default tags

    def test_todo_creation_with_none_tags(self):
        """Test that None tags are converted to empty list."""
        todo = Todo(
            id="test-id",
            title="Test Task",
            description="Test Description",
            tags=None
        )

        self.assertEqual(todo.tags, [])

    def test_todo_invalid_priority_defaults_to_medium(self):
        """Test that invalid priority defaults to medium."""
        todo = Todo(
            id="test-id",
            title="Test Task",
            description="Test Description",
            priority="invalid"
        )

        self.assertEqual(todo.priority, "medium")

    def test_todo_post_init_handling(self):
        """Test __post_init__ handling of default values."""
        todo = Todo(
            id="test-id",
            title="Test Task",
            description="Test Description",
            priority="low",
            tags=None
        )

        # Check that tags are initialized to empty list
        self.assertEqual(todo.tags, [])
        self.assertEqual(todo.priority, "low")

    def test_todo_with_empty_tags_list(self):
        """Test Todo with empty tags list."""
        todo = Todo(
            id="test-id",
            title="Test Task",
            description="Test Description",
            tags=[]
        )

        self.assertEqual(todo.tags, [])


class TestTodoModelService(unittest.TestCase):
    """Test cases for TodoModel service with priority and tags."""

    def setUp(self):
        """Set up a fresh TodoModel for each test."""
        self.model = TodoModel()

    def test_add_todo_with_priority_and_tags(self):
        """Test adding a todo with priority and tags."""
        todo = self.model.add_todo(
            title="Test Task",
            description="Test Description",
            priority="high",
            tags=["work", "urgent"]
        )

        self.assertEqual(todo.title, "Test Task")
        self.assertEqual(todo.description, "Test Description")
        self.assertEqual(todo.priority, "high")
        self.assertEqual(todo.tags, ["work", "urgent"])
        self.assertIn(todo.id, self.model.todos)

    def test_add_todo_with_default_priority_and_tags(self):
        """Test adding a todo with default priority and tags."""
        todo = self.model.add_todo(
            title="Test Task",
            description="Test Description"
        )

        self.assertEqual(todo.priority, "medium")
        self.assertEqual(todo.tags, [])

    def test_update_todo_priority_and_tags(self):
        """Test updating todo priority and tags."""
        todo = self.model.add_todo(
            title="Test Task",
            description="Test Description",
            priority="low",
            tags=["personal"]
        )

        updated_todo = self.model.update_todo(
            todo_id=todo.id,
            priority="high",
            tags=["work", "urgent"]
        )

        self.assertEqual(updated_todo.priority, "high")
        self.assertEqual(updated_todo.tags, ["work", "urgent"])

    def test_update_todo_partial_fields(self):
        """Test updating only some fields of a todo."""
        todo = self.model.add_todo(
            title="Test Task",
            description="Test Description",
            priority="low",
            tags=["personal"]
        )

        # Update only priority, keep other fields unchanged
        updated_todo = self.model.update_todo(
            todo_id=todo.id,
            priority="high"
        )

        self.assertEqual(updated_todo.title, "Test Task")
        self.assertEqual(updated_todo.description, "Test Description")
        self.assertEqual(updated_todo.priority, "high")  # Changed
        self.assertEqual(updated_todo.tags, ["personal"])  # Unchanged

    def test_get_all_todos_with_priority_and_tags(self):
        """Test retrieving all todos with priority and tags."""
        self.model.add_todo("Task 1", "Description 1", "high", ["work"])
        self.model.add_todo("Task 2", "Description 2", "low", ["personal"])

        todos = self.model.get_all_todos()

        self.assertEqual(len(todos), 2)

        # Check that priority and tags are preserved
        priorities = [todo.priority for todo in todos]
        self.assertIn("high", priorities)
        self.assertIn("low", priorities)

        all_tags = [tag for todo in todos for tag in todo.tags]
        self.assertIn("work", all_tags)
        self.assertIn("personal", all_tags)


if __name__ == "__main__":
    unittest.main()