#!/usr/bin/env python3
"""Performance tests for search/filter operations with 100+ tasks."""

import time
from src.todo.services import TodoService


def test_performance_search_filter_100_plus_tasks():
    """T056: Test performance with 100+ tasks for search/filter operations."""
    service = TodoService()

    # Add 150 tasks for performance testing
    print("Adding 150 tasks for performance testing...")
    start_time = time.time()
    for i in range(150):
        priority = ["high", "medium", "low"][i % 3]
        tags = ["work", "personal", "urgent"] if i % 3 == 0 else ["project", "review"]
        service.add_task(f"Task {i}", f"Description for task {i}", priority, tags)
    add_time = time.time() - start_time
    print(f"Added 150 tasks in {add_time:.4f} seconds")

    # Test search performance
    print("Testing search performance...")
    start_time = time.time()
    results = service.search_tasks("task")
    search_time = time.time() - start_time
    print(f"Search found {len(results)} results in {search_time:.4f} seconds")

    # Test filter by status performance
    print("Testing filter by status performance...")
    start_time = time.time()
    results = service.filter_by_status("incomplete")
    filter_status_time = time.time() - start_time
    print(f"Status filter found {len(results)} results in {filter_status_time:.4f} seconds")

    # Test filter by priority performance
    print("Testing filter by priority performance...")
    start_time = time.time()
    results = service.filter_by_priority("high")
    filter_priority_time = time.time() - start_time
    print(f"Priority filter found {len(results)} results in {filter_priority_time:.4f} seconds")

    # Test filter by tag performance
    print("Testing filter by tag performance...")
    start_time = time.time()
    results = service.filter_by_tag("work")
    filter_tag_time = time.time() - start_time
    print(f"Tag filter found {len(results)} results in {filter_tag_time:.4f} seconds")

    # Test combined filters performance
    print("Testing combined filters performance...")
    start_time = time.time()
    results = service.combine_filters(status="incomplete", priority="high", tag="work")
    combined_filter_time = time.time() - start_time
    print(f"Combined filters found {len(results)} results in {combined_filter_time:.4f} seconds")

    # Performance expectations: all operations should complete in reasonable time
    assert search_time < 1.0, f"Search took too long: {search_time:.4f}s"
    assert filter_status_time < 1.0, f"Status filter took too long: {filter_status_time:.4f}s"
    assert filter_priority_time < 1.0, f"Priority filter took too long: {filter_priority_time:.4f}s"
    assert filter_tag_time < 1.0, f"Tag filter took too long: {filter_tag_time:.4f}s"
    assert combined_filter_time < 1.0, f"Combined filters took too long: {combined_filter_time:.4f}s"

    print("+ Performance tests passed - all operations completed efficiently")


def test_performance_sort_100_plus_tasks():
    """T057: Test performance with 100+ tasks for sort operations."""
    service = TodoService()

    # Add 150 tasks for performance testing
    print("Adding 150 tasks for sort performance testing...")
    for i in range(150):
        priority = ["high", "medium", "low"][i % 3]
        service.add_task(f"Task {i:03d}", f"Description for task {i}", priority, ["test"])

    all_tasks = service.list_tasks()
    print(f"Created {len(all_tasks)} tasks for sorting")

    # Test sort by priority performance
    print("Testing sort by priority performance...")
    start_time = time.time()
    sorted_tasks = service.sort_tasks(all_tasks, "priority", ascending=True)
    sort_priority_time = time.time() - start_time
    print(f"Sorted by priority in {sort_priority_time:.4f} seconds")

    # Test sort by title performance
    print("Testing sort by title performance...")
    start_time = time.time()
    sorted_tasks = service.sort_tasks(all_tasks, "title", ascending=True)
    sort_title_time = time.time() - start_time
    print(f"Sorted by title in {sort_title_time:.4f} seconds")

    # Test sort by ID performance
    print("Testing sort by ID performance...")
    start_time = time.time()
    sorted_tasks = service.sort_tasks(all_tasks, "id", ascending=True)
    sort_id_time = time.time() - start_time
    print(f"Sorted by ID in {sort_id_time:.4f} seconds")

    # Performance expectations: all operations should complete in reasonable time
    assert sort_priority_time < 1.0, f"Priority sort took too long: {sort_priority_time:.4f}s"
    assert sort_title_time < 1.0, f"Title sort took too long: {sort_title_time:.4f}s"
    assert sort_id_time < 1.0, f"ID sort took too long: {sort_id_time:.4f}s"

    print("+ Sort performance tests passed - all operations completed efficiently")


if __name__ == "__main__":
    print("Running performance tests...")
    test_performance_search_filter_100_plus_tasks()
    print()
    test_performance_sort_100_plus_tasks()
    print("\nAll performance tests passed!")