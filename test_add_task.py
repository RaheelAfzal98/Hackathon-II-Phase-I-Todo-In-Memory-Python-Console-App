"""Test script to verify adding tasks works within a single session."""
from src.todo.services import TodoService

# Create a service instance
service = TodoService()

# Add a task
task = service.add_task("Test Task", "Test Description")
print(f"Added task: {task.id} - {task.title}")

# List all tasks
tasks = service.list_tasks()
print(f"Total tasks: {len(tasks)}")
for t in tasks:
    print(f"  - {t.id[:8]}: {t.title} (Completed: {t.completed})")