#!/usr/bin/env python3
"""Test script to verify todo application functionality."""

from src.todo.services import TodoService

def test_basic_functionality():
    """Test basic todo functionality."""
    print("Testing Todo Application Functionality")
    print("=" * 40)

    # Create a service instance
    service = TodoService()

    # Test adding a task
    print("\n1. Testing task addition...")
    task = service.add_task("Test Task", "This is a test task", "high", ["work", "test"])
    print(f"+ Added task: {task.title} with ID: {task.id[:8]}")

    # Test adding another task
    task2 = service.add_task("Second Task", "This is another test task", "medium", ["personal"])
    print(f"+ Added task: {task2.title} with ID: {task2.id[:8]}")

    # Test listing tasks
    print("\n2. Testing task listing...")
    tasks = service.list_tasks()
    print(f"+ Found {len(tasks)} tasks")
    for task in tasks:
        status = "Completed" if task.completed else "Incomplete"
        print(f"  - {task.title} [{status}]")

    # Test updating a task
    print("\n3. Testing task update...")
    updated_task = service.update_task(task.id, title="Updated Test Task", priority="low")
    if updated_task:
        print(f"+ Updated task: {updated_task.title} with priority {updated_task.priority}")
    else:
        print("- Failed to update task")

    # Test marking as complete
    print("\n4. Testing task completion...")
    completed_task = service.toggle_task_completion(task.id)
    if completed_task:
        print(f"+ Toggled completion for task: {completed_task.title} (now {'completed' if completed_task.completed else 'incomplete'})")
    else:
        print("- Failed to toggle task completion")

    # Test filtering
    print("\n5. Testing task filtering...")
    completed_tasks = service.filter_by_status("completed")
    print(f"+ Found {len(completed_tasks)} completed tasks")

    incomplete_tasks = service.filter_by_status("incomplete")
    print(f"+ Found {len(incomplete_tasks)} incomplete tasks")

    # Test searching
    print("\n6. Testing task search...")
    search_results = service.search_tasks("test")
    print(f"+ Found {len(search_results)} tasks matching 'test'")

    # Test sorting
    print("\n7. Testing task sorting...")
    all_tasks = service.list_tasks()
    sorted_tasks = service.sort_tasks(all_tasks, "priority", ascending=False)  # High priority first
    print(f"+ Sorted {len(sorted_tasks)} tasks by priority")
    for task in sorted_tasks:
        print(f"  - {task.title} (Priority: {task.priority})")

    # Test deletion
    print("\n8. Testing task deletion...")
    delete_success = service.delete_task(task.id)
    if delete_success:
        print(f"+ Deleted task with ID: {task.id[:8]}")
    else:
        print("- Failed to delete task")

    # Verify deletion
    remaining_tasks = service.list_tasks()
    print(f"+ Remaining tasks after deletion: {len(remaining_tasks)}")

    print("\n" + "=" * 40)
    print("All tests completed successfully! +")

if __name__ == "__main__":
    test_basic_functionality()