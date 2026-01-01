#!/usr/bin/env python3
"""
Demo script showing the complete functionality of the todo application.
This demonstrates that all features work correctly within a single session.
"""

from src.todo.services import TodoService

def main():
    print("=== Todo Application Demo ===\n")

    # Create a service instance
    service = TodoService()

    print("1. ADDING TASKS:")
    task1 = service.add_task("Complete Project", "Finish the todo application project")
    print(f"   + Added: {task1.title}")

    task2 = service.add_task("Write Documentation", "Document the todo application")
    print(f"   + Added: {task2.title}")

    print(f"\n   Total tasks after adding: {len(service.list_tasks())}")

    print("\n2. VIEWING ALL TASKS:")
    tasks = service.list_tasks()
    for i, task in enumerate(tasks, 1):
        status = "[X] Completed" if task.completed else "[ ] Incomplete"
        print(f"   {i}. {status} {task.id[:8]} - {task.title}")
        print(f"      {task.description}")

    print("\n3. UPDATING A TASK:")
    updated_task = service.update_task(task1.id, "Complete Todo Project", "Finish the todo application project with all features")
    print(f"   + Updated: {updated_task.title}")

    print("\n4. TOGGLING COMPLETION STATUS:")
    completed_task = service.toggle_task_completion(task1.id)
    print(f"   + Task marked as: {'completed' if completed_task.completed else 'incomplete'}")

    # Verify the status change
    tasks = service.list_tasks()
    for task in tasks:
        status = "[X] Completed" if task.completed else "[ ] Incomplete"
        print(f"      {status} {task.title}")

    print("\n5. DELETING A TASK:")
    result = service.delete_task(task2.id)
    print(f"   + Task deleted: {result}")

    print(f"\n   Total tasks after deletion: {len(service.list_tasks())}")

    print("\n6. FINAL STATE:")
    final_tasks = service.list_tasks()
    if final_tasks:
        for task in final_tasks:
            status = "[X] Completed" if task.completed else "[ ] Incomplete"
            print(f"   {status} {task.title}")
    else:
        print("   No tasks remaining")

    print("\n=== Demo completed successfully! ===")

if __name__ == "__main__":
    main()