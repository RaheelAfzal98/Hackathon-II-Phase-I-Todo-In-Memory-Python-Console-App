"""Final integration test to verify all user stories work correctly."""
from src.todo.services import TodoService


def test_user_story_1_add_task():
    """Test User Story 1: Add Todo Task"""
    print("Testing User Story 1: Add Todo Task...")
    service = TodoService()

    # Test adding a task with title and description
    task = service.add_task("Integration Test Task", "Test description for integration")
    assert task.title == "Integration Test Task"
    assert task.description == "Test description for integration"
    assert task.completed is False
    print("  [OK] Task added with title and description")

    # Test adding a task with empty description (should be allowed)
    task2 = service.add_task("Task with empty description", "")
    assert task2.title == "Task with empty description"
    assert task2.description == ""
    print("  [OK] Task added with empty description")

    # Test validation: adding task without title should raise ValueError
    try:
        service.add_task("", "This should fail")
        assert False, "Expected ValueError for empty title"
    except ValueError as e:
        assert str(e) == "Title is required"
        print("  [OK] Validation works: empty title raises ValueError")

    return service


def test_user_story_2_view_tasks():
    """Test User Story 2: View All Tasks"""
    print("Testing User Story 2: View All Tasks...")
    service = TodoService()

    # Add some tasks first
    task1 = service.add_task("First Task", "Description 1")
    task2 = service.add_task("Second Task", "Description 2")

    # Test viewing all tasks
    tasks = service.list_tasks()
    assert len(tasks) == 2
    titles = [task.title for task in tasks]
    assert "First Task" in titles
    assert "Second Task" in titles
    print("  [OK] All tasks listed correctly")

    # Verify task details
    for task in tasks:
        assert hasattr(task, 'id')
        assert hasattr(task, 'title')
        assert hasattr(task, 'description')
        assert hasattr(task, 'completed')
    print("  [OK] All task details are accessible")


def test_user_story_3_update_task():
    """Test User Story 3: Update Task"""
    print("Testing User Story 3: Update Task...")
    service = TodoService()

    # Add a task to update
    original_task = service.add_task("Original Title", "Original Description")

    # Test updating both title and description
    updated_task = service.update_task(original_task.id, "Updated Title", "Updated Description")
    assert updated_task.title == "Updated Title"
    assert updated_task.description == "Updated Description"
    print("  [OK] Task updated with new title and description")

    # Test updating only title
    updated_task2 = service.update_task(original_task.id, "Another Updated Title")
    assert updated_task2.title == "Another Updated Title"
    assert updated_task2.description == "Updated Description"  # Should remain unchanged
    print("  [OK] Task updated with new title only")

    # Test updating only description
    updated_task3 = service.update_task(original_task.id, description="New Description")
    assert updated_task3.title == "Another Updated Title"  # Should remain unchanged
    assert updated_task3.description == "New Description"
    print("  [OK] Task updated with new description only")

    # Test validation: updating with empty title should raise ValueError
    try:
        service.update_task(original_task.id, "")
        assert False, "Expected ValueError for empty title"
    except ValueError as e:
        assert str(e) == "Title cannot be empty"
        print("  [OK] Validation works: empty title raises ValueError")


def test_user_story_4_delete_task():
    """Test User Story 4: Delete Task"""
    print("Testing User Story 4: Delete Task...")
    service = TodoService()

    # Add a task to delete
    task = service.add_task("Task to Delete", "Description")

    # Verify task exists before deletion
    tasks = service.list_tasks()
    assert len(tasks) == 1

    # Delete the task
    result = service.delete_task(task.id)
    assert result is True
    print("  [OK] Task deleted successfully")

    # Verify task no longer exists
    tasks_after = service.list_tasks()
    assert len(tasks_after) == 0
    print("  [OK] Task no longer appears in task list after deletion")

    # Test deleting non-existent task
    result = service.delete_task("non-existent-id")
    assert result is False
    print("  [OK] Deleting non-existent task returns False")


def test_user_story_5_toggle_completion():
    """Test User Story 5: Mark Task Complete/Incomplete"""
    print("Testing User Story 5: Mark Task Complete/Incomplete...")
    service = TodoService()

    # Add a task
    task = service.add_task("Task to Toggle", "Description")
    assert task.completed is False

    # Toggle to complete
    completed_task = service.toggle_task_completion(task.id)
    assert completed_task.completed is True
    print("  [OK] Task marked as complete")

    # Toggle back to incomplete
    incomplete_task = service.toggle_task_completion(task.id)
    assert incomplete_task.completed is False
    print("  [OK] Task marked as incomplete")

    # Test with non-existent task
    result = service.toggle_task_completion("non-existent-id")
    assert result is None
    print("  [OK] Toggling non-existent task returns None")


def test_edge_cases():
    """Test edge cases and error handling"""
    print("Testing edge cases and error handling...")
    service = TodoService()

    # Test operations on non-existent tasks
    assert service.get_task("non-existent-id") is None
    print("  [OK] Getting non-existent task returns None")

    assert service.update_task("non-existent-id", "New Title") is None
    print("  [OK] Updating non-existent task returns None")

    assert service.delete_task("non-existent-id") is False
    print("  [OK] Deleting non-existent task returns False")

    assert service.toggle_task_completion("non-existent-id") is None
    print("  [OK] Toggling completion of non-existent task returns None")


def run_final_integration_test():
    """Run all integration tests for all user stories."""
    print("Running final integration test for all user stories...\n")

    # Test each user story
    test_user_story_1_add_task()
    print()

    test_user_story_2_view_tasks()
    print()

    test_user_story_3_update_task()
    print()

    test_user_story_4_delete_task()
    print()

    test_user_story_5_toggle_completion()
    print()

    test_edge_cases()
    print()

    print("All user stories have been tested successfully!")
    print("All features work correctly together as a complete system.")
    return True


if __name__ == "__main__":
    success = run_final_integration_test()
    if success:
        print("\nFinal integration test: PASSED")
    else:
        print("\nFinal integration test: FAILED")