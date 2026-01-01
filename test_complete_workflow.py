"""Test script to verify complete user workflows work together."""
from src.todo.services import TodoService

def test_complete_workflow():
    print("Testing complete user workflow...")

    # Create a service instance
    service = TodoService()

    # Step 1: Add a task
    task1 = service.add_task("Complete Project", "Finish the todo app implementation")
    print(f"[OK] Added task: {task1.title}")

    # Step 2: Add another task
    task2 = service.add_task("Write Tests", "Create comprehensive tests for all features")
    print(f"[OK] Added task: {task2.title}")

    # Step 3: View all tasks
    all_tasks = service.list_tasks()
    print(f"[OK] Listed tasks: {len(all_tasks)} tasks found")

    # Step 4: Update a task
    updated_task = service.update_task(task1.id, "Complete Todo App Project", "Finish the todo app implementation and test all features")
    print(f"[OK] Updated task: {updated_task.title}")

    # Step 5: Mark a task as complete
    completed_task = service.toggle_task_completion(task1.id)
    print(f"[OK] Toggled completion status: {completed_task.title} (Completed: {completed_task.completed})")

    # Step 6: Verify the completion status
    all_tasks = service.list_tasks()
    for task in all_tasks:
        print(f"  - {task.title} (Completed: {task.completed})")

    # Step 7: Delete a task
    result = service.delete_task(task2.id)
    print(f"[OK] Deleted task: {result}")

    # Step 8: Verify final task list
    final_tasks = service.list_tasks()
    print(f"[OK] Final task list: {len(final_tasks)} tasks remain")

    # Final verification
    if len(final_tasks) == 1 and final_tasks[0].completed:
        print("[OK] All features work together correctly!")
        return True
    else:
        print("[FAILED] Workflow test failed!")
        return False

if __name__ == "__main__":
    success = test_complete_workflow()
    if success:
        print("\nComplete workflow test: PASSED")
    else:
        print("\nComplete workflow test: FAILED")