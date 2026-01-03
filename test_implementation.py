#!/usr/bin/env python3
"""Test script to validate the implementation of intermediate features."""

from src.todo.services import TodoService
from src.todo.models import Todo

def test_priority_and_tags():
    """Test priority and tags functionality."""
    print("Testing Priority and Tags functionality...")

    service = TodoService()

    # Test creating a task with priority and tags
    task = service.add_task(
        title="Test task",
        description="Test description",
        priority="high",
        tags=["work", "urgent"]
    )

    assert task.priority == "high", f"Expected priority 'high', got '{task.priority}'"
    assert "work" in task.tags, f"Expected 'work' in tags {task.tags}"
    assert "urgent" in task.tags, f"Expected 'urgent' in tags {task.tags}"
    print("+ Created task with priority and tags")

    # Test updating priority and tags
    updated_task = service.update_task(
        task_id=task.id,
        title="Updated test task",
        priority="low",
        tags=["personal"]
    )

    assert updated_task.priority == "low", f"Expected priority 'low', got '{updated_task.priority}'"
    assert "personal" in updated_task.tags, f"Expected 'personal' in tags {updated_task.tags}"
    assert len(updated_task.tags) == 1, f"Expected 1 tag, got {len(updated_task.tags)}"
    print("+ Updated task priority and tags")

    print("Priority and Tags functionality test passed!\n")


def test_search_functionality():
    """Test search functionality."""
    print("Testing Search functionality...")

    service = TodoService()

    # Add some test tasks
    service.add_task("Project Alpha", "Important project", "high", ["work", "project"])
    service.add_task("Buy groceries", "Milk and bread", "medium", ["personal"])
    service.add_task("Fix bug", "Critical bug fix", "high", ["work", "urgent"])

    # Search for "project"
    results = service.search_tasks("project")
    assert len(results) == 1, f"Expected 1 result for 'project', got {len(results)}"
    assert "Project Alpha" in [task.title for task in results]
    print("+ Search for 'project' returned correct results")

    # Search for "work"
    results = service.search_tasks("work")
    assert len(results) == 2, f"Expected 2 results for 'work', got {len(results)}"
    titles = [task.title for task in results]
    assert "Project Alpha" in titles
    assert "Fix bug" in titles
    print("+ Search for 'work' returned correct results")

    print("Search functionality test passed!\n")


def test_filter_functionality():
    """Test filter functionality."""
    print("Testing Filter functionality...")

    service = TodoService()

    # Clear existing tasks and add test tasks
    # We'll use a fresh service instance for clean testing
    service = TodoService()
    service.add_task("Urgent task", "Very important", "high", ["urgent"])
    service.add_task("Normal task", "Regular task", "medium", ["work"])
    service.add_task("Low priority", "Not urgent", "low", ["low"])

    # Filter by priority "high"
    high_priority_tasks = service.filter_by_priority("high")
    assert len(high_priority_tasks) == 1, f"Expected 1 high priority task, got {len(high_priority_tasks)}"
    assert high_priority_tasks[0].priority == "high"
    print("+ Filter by high priority works")

    # Filter by tag "urgent"
    urgent_tasks = service.filter_by_tag("urgent")
    assert len(urgent_tasks) == 1, f"Expected 1 urgent task, got {len(urgent_tasks)}"
    assert "urgent" in urgent_tasks[0].tags
    print("+ Filter by urgent tag works")

    # Mark one task as completed and test status filter
    task_to_complete = service.list_tasks()[0]
    service.mark_task_complete(task_to_complete.id)

    completed_tasks = service.filter_by_status("completed")
    assert len(completed_tasks) == 1, f"Expected 1 completed task, got {len(completed_tasks)}"
    print("+ Filter by completion status works")

    print("Filter functionality test passed!\n")


def test_sort_functionality():
    """Test sort functionality."""
    print("Testing Sort functionality...")

    service = TodoService()

    # Clear and add tasks for sorting test
    service = TodoService()
    service.add_task("Zebra task", "Last alphabetically", "low")
    service.add_task("Apple task", "First alphabetically", "high")
    service.add_task("Middle task", "In the middle", "medium")

    all_tasks = service.list_tasks()
    assert len(all_tasks) == 3, f"Expected 3 tasks, got {len(all_tasks)}"

    # Sort by priority (high should come first)
    sorted_by_priority = service.sort_tasks(all_tasks, "priority", ascending=False)  # high to low
    assert sorted_by_priority[0].priority == "high", f"Expected high priority first, got {sorted_by_priority[0].priority}"
    print("+ Sort by priority works")

    # Sort by title (alphabetical)
    sorted_by_title = service.sort_tasks(all_tasks, "title", ascending=True)
    assert sorted_by_title[0].title == "Apple task", f"Expected 'Apple task' first, got {sorted_by_title[0].title}"
    print("+ Sort by title works")

    print("Sort functionality test passed!\n")


def main():
    """Run all tests."""
    print("Starting validation of intermediate features implementation...\n")

    try:
        test_priority_and_tags()
        test_search_functionality()
        test_filter_functionality()
        test_sort_functionality()

        print("All tests passed! Implementation is working correctly.")
        print("All intermediate features (Priorities & Tags, Search & Filter, Sort) are implemented successfully.")

    except AssertionError as e:
        print(f"Test failed: {e}")
        return 1
    except Exception as e:
        print(f"Error during testing: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())