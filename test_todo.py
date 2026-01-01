# Test the todo application

from src.todo.services import TodoService

# Create a service instance
service = TodoService()

# Test adding a task
task = service.add_task("Test Task", "This is a test task")
print(f"Added task: {task.title}")

# List all tasks
tasks = service.list_tasks()
print(f"Total tasks: {len(tasks)}")

# Update the task
updated_task = service.update_task(task.id, "Updated Test Task", "This is an updated test task")
print(f"Updated task: {updated_task.title}")

# Toggle completion
completed_task = service.toggle_task_completion(task.id)
print(f"Task completed: {completed_task.completed}")

# List all tasks again
tasks = service.list_tasks()
for t in tasks:
    print(f"- {t.title} (Completed: {t.completed})")

# Delete the task
result = service.delete_task(task.id)
print(f"Task deleted: {result}")

# List all tasks (should be empty)
tasks = service.list_tasks()
print(f"Total tasks after deletion: {len(tasks)}")