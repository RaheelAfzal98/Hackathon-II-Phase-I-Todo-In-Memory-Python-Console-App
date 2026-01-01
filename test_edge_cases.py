"""Test script to verify edge cases are handled properly."""
from src.todo.services import TodoService

# Create a service instance
service = TodoService()

print("Testing edge cases...")

# Test 1: Invalid task ID for update
result = service.update_task("invalid-id", "New Title", "New Description")
print(f"Update with invalid ID: {result is None}")

# Test 2: Invalid task ID for delete
result = service.delete_task("invalid-id")
print(f"Delete with invalid ID: {result is False}")

# Test 3: Invalid task ID for toggle completion
result = service.toggle_task_completion("invalid-id")
print(f"Toggle completion with invalid ID: {result is None}")

# Test 4: Empty title validation in add_task
try:
    service.add_task("", "Valid Description")
    print("Empty title validation: FAILED")
except ValueError:
    print("Empty title validation: PASSED")

# Test 5: Empty description is allowed for add_task
try:
    task = service.add_task("Valid Title", "")
    print("Empty description allowed: PASSED")
except ValueError:
    print("Empty description allowed: FAILED")

# Test 6: Non-existent task for viewing
tasks = service.list_tasks()
print(f"List with no tasks: {len(tasks) == 1}")  # Should be 1 now because of the valid task added above

print("Edge case testing completed.")