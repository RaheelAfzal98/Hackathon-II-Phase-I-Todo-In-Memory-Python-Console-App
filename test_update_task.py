"""Test script to verify updating tasks works correctly."""
from src.todo.services import TodoService

# Create a service instance
service = TodoService()

# Add a task first
task = service.add_task("Original Title", "Original Description")
print(f"Added task: {task.id} - {task.title} | {task.description}")

# Update the task
updated_task = service.update_task(task.id, "Updated Title", "Updated Description")
print(f"Updated task: {updated_task.id} - {updated_task.title} | {updated_task.description}")

# Verify the update worked
tasks = service.list_tasks()
for t in tasks:
    print(f"Verification: {t.id} - {t.title} | {t.description}")