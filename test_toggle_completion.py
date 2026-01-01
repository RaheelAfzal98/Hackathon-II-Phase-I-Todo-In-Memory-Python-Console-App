"""Test script to verify toggling task completion works correctly."""
from src.todo.services import TodoService

# Create a service instance
service = TodoService()

# Add a task first
task = service.add_task("Test Task", "Test Description")
print(f"Added task: {task.id} - {task.title} (Completed: {task.completed})")

# Toggle completion status
toggled_task = service.toggle_task_completion(task.id)
print(f"Toggled task: {toggled_task.id} - {toggled_task.title} (Completed: {toggled_task.completed})")

# Toggle completion status again
toggled_task2 = service.toggle_task_completion(task.id)
print(f"Toggled task again: {toggled_task2.id} - {toggled_task2.title} (Completed: {toggled_task2.completed})")