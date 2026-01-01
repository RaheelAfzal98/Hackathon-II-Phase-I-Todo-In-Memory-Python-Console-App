"""Test script to verify viewing tasks works correctly."""
from src.todo.services import TodoService

# Create a service instance
service = TodoService()

# Add a task first
task = service.add_task("Test Task", "Test Description")
print(f"Added task: {task.id} - {task.title}")

# List all tasks
tasks = service.list_tasks()
print(f"\nTotal tasks: {len(tasks)}")
for t in tasks:
    print(f"  - ID: {t.id[:8]}")
    print(f"    Title: {t.title}")
    print(f"    Description: {t.description}")
    print(f"    Completed: {t.completed}")