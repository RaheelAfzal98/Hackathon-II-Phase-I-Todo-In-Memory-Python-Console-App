#!/usr/bin/env python3
"""Test script to verify the todo application functionality."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from todo.services import TodoService

def test_todo_functionality():
    """Test the basic functionality of the todo service."""
    print("Testing Todo Application...")

    # Create a service instance
    service = TodoService()

    # Test adding a task
    print("\n1. Testing add_task functionality:")
    task1 = service.add_task("Test Task 1", "This is a test task")
    print(f"   Added task: {task1.id[:8]} - {task1.title}")

    # Add another task
    task2 = service.add_task("Test Task 2", "This is another test task")
    print(f"   Added task: {task2.id[:8]} - {task2.title}")

    # Test listing tasks
    print("\n2. Testing list_tasks functionality:")
    tasks = service.list_tasks()
    print(f"   Found {len(tasks)} tasks:")
    for task in tasks:
        status = "[X]" if task.completed else "[ ]"
        print(f"   {status} {task.id[:8]} - {task.title}")

    # Test updating a task
    print("\n3. Testing update_task functionality:")
    updated_task = service.update_task(task1.id, title="Updated Task 1", description="Updated description")
    if updated_task:
        print(f"   Updated task: {updated_task.id[:8]} - {updated_task.title}")

    # Test toggling completion
    print("\n4. Testing toggle_task_completion functionality:")
    completed_task = service.toggle_task_completion(task1.id)
    if completed_task:
        print(f"   Toggled task completion: {completed_task.id[:8]} - {completed_task.title} (now {completed_task.completed})")

    # Test getting a specific task
    print("\n5. Testing get_task functionality:")
    retrieved_task = service.get_task(task1.id)
    if retrieved_task:
        print(f"   Retrieved task: {retrieved_task.id[:8]} - {retrieved_task.title}")

    # Test deleting a task
    print("\n6. Testing delete_task functionality:")
    delete_success = service.delete_task(task2.id)
    print(f"   Delete task result: {delete_success}")

    # List tasks again to see the result
    print("\n7. Final task list:")
    final_tasks = service.list_tasks()
    print(f"   Found {len(final_tasks)} tasks:")
    for task in final_tasks:
        status = "[X]" if task.completed else "[ ]"
        print(f"   {status} {task.id[:8]} - {task.title}")

if __name__ == "__main__":
    test_todo_functionality()