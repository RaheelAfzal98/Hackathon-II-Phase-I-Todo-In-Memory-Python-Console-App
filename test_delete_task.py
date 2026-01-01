"""Test script to verify deleting tasks works correctly."""
from src.todo.services import TodoService

# Create a service instance
service = TodoService()

# Add a task first
task = service.add_task("Task to Delete", "This task will be deleted")
print(f"Added task: {task.id} - {task.title}")

# List tasks before deletion
tasks_before = service.list_tasks()
print(f"Tasks before deletion: {len(tasks_before)}")

# Delete the task
result = service.delete_task(task.id)
print(f"Delete operation successful: {result}")

# List tasks after deletion
tasks_after = service.list_tasks()
print(f"Tasks after deletion: {len(tasks_after)}")

if len(tasks_after) == 0:
    print("Success: Task was properly removed from storage")
else:
    print("Error: Task still exists in storage")
    for t in tasks_after:
        print(f"  - {t.id} - {t.title}")