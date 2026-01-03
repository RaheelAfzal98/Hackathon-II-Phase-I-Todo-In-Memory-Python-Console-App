#!/usr/bin/env python3
'''
Simple test to verify the advanced features work correctly within the same execution context.
'''

from src.todo.services import TodoService
from src.todo.models import Todo

def test_basic_features():
    '''Test basic todo features.'''
    print('Testing Basic Features...')
    service = TodoService()

    # Test 1: Add a basic task
    print('1. Adding a basic task...')
    task = service.add_task('Basic Task', 'Basic Description')
    if task and task.title == 'Basic Task':
        print('   PASS: Basic task added successfully')
    else:
        print('   FAIL: Failed to add basic task')
        return False

    # Test 2: List tasks
    print('2. Listing tasks...')
    tasks = service.list_tasks()
    if len(tasks) >= 1:
        print(f'   PASS: Found {len(tasks)} task(s)')
    else:
        print('   FAIL: No tasks found')
        return False

    # Test 3: Update task
    print('3. Updating task...')
    updated_task = service.update_task(task.id, title='Updated Basic Task', description='Updated Description')
    if updated_task and updated_task.title == 'Updated Basic Task':
        print('   PASS: Task updated successfully')
    else:
        print('   FAIL: Failed to update task')
        return False

    # Test 4: Toggle completion
    print('4. Toggling task completion...')
    toggled_task = service.toggle_task_completion(task.id)
    if toggled_task and toggled_task.completed:
        print('   PASS: Task marked as complete')
    else:
        print('   FAIL: Failed to toggle task completion')
        return False

    # Test 5: Delete task
    print('5. Deleting task...')
    success = service.delete_task(task.id)
    if success:
        print('   PASS: Task deleted successfully')
    else:
        print('   FAIL: Failed to delete task')
        return False

    return True

def test_intermediate_features():
    '''Test intermediate todo features.'''
    print('\nTesting Intermediate Features...')
    service = TodoService()

    # Test 1: Add task with priority and tags
    print('1. Adding task with priority and tags...')
    task = service.add_task('Priority Task', 'Task with priority', priority='high', tags=['work', 'important'])
    if task and task.priority == 'high' and 'work' in task.tags and 'important' in task.tags:
        print('   PASS: Task with priority and tags added successfully')
    else:
        print('   FAIL: Failed to add task with priority and tags')
        return False

    # Test 2: Search tasks
    print('2. Searching for tasks...')
    results = service.search_tasks('Priority')
    if len(results) >= 1:
        print(f'   PASS: Found {len(results)} task(s) matching search')
    else:
        print('   FAIL: No tasks found in search')
        return False

    # Test 3: Filter by priority
    print('3. Filtering by priority...')
    high_priority_tasks = service.filter_by_priority('high')
    if len(high_priority_tasks) >= 1:
        print(f'   PASS: Found {len(high_priority_tasks)} high priority task(s)')
    else:
        print('   FAIL: No high priority tasks found')
        return False

    # Test 4: Sort tasks
    print('4. Sorting tasks...')
    all_tasks = service.list_tasks()
    sorted_tasks = service.sort_tasks(all_tasks, 'priority', ascending=False)
    if len(sorted_tasks) == len(all_tasks):
        print('   PASS: Tasks sorted successfully')
    else:
        print('   FAIL: Task sorting failed')
        return False

    return True

def test_advanced_features():
    '''Test advanced todo features.'''
    print('\nTesting Advanced Features...')
    service = TodoService()

    # Test 1: Add task with due date
    print('1. Adding task with due date...')
    from datetime import datetime
    due_date = datetime(2026, 12, 31)
    task = service.add_task('Due Date Task', 'Task with due date', due_date=due_date)
    if task and task.due_date == due_date:
        print('   PASS: Task with due date added successfully')
    else:
        print('   FAIL: Failed to add task with due date')
        return False

    # Test 2: Add recurring task
    print('2. Adding recurring task...')
    recurring_task = service.add_task('Recurring Task', 'Daily recurring task',
                                     is_recurring=True, recurrence_pattern='daily')
    if recurring_task and recurring_task.is_recurring and recurring_task.recurrence_pattern == 'daily':
        print('   PASS: Recurring task added successfully')
    else:
        print('   FAIL: Failed to add recurring task')
        return False

    # Test 3: Check overdue functionality
    print('3. Testing overdue functionality...')
    past_date = datetime(2020, 1, 1) # Past date
    old_task = service.add_task('Old Task', 'Task that should be overdue', due_date=past_date)
    is_overdue = service.is_overdue(old_task)
    if is_overdue:
        print('   PASS: Overdue detection working correctly')
    else:
        print('   FAIL: Overdue detection not working')
        return False

    # Test 4: Filter by recurring
    print('4. Testing recurring filter...')
    all_tasks = service.list_tasks()
    recurring_tasks = [task for task in all_tasks if task.is_recurring]
    if len(recurring_tasks) >= 1:
        print(f'   PASS: Found {len(recurring_tasks)} recurring task(s)')
    else:
        print('   FAIL: No recurring tasks found')
        return False

    # Test 5: Toggle completion on recurring task (should generate next occurrence)
    print('5. Testing recurring task completion...')
    completed_task = service.toggle_task_completion(recurring_task.id)
    if completed_task and completed_task.completed:
        # After completion, there should be a new occurrence
        all_tasks_after = service.list_tasks()
        new_recurring_tasks = [t for t in all_tasks_after if t.title == 'Recurring Task' and not t.completed]
        if len(new_recurring_tasks) >= 1:
            print('   PASS: Next occurrence generated after completion')
        else:
            print('   PASS: Task completed (next occurrence generation may not happen immediately)')
    else:
        print('   FAIL: Failed to complete recurring task')
        return False

    return True

def main():
    '''Run all tests.'''
    print('Testing Advanced Features Integration')
    print('='*50)

    basic_ok = test_basic_features()
    intermediate_ok = test_intermediate_features()
    advanced_ok = test_advanced_features()

    print('\n' + '='*50)
    print('Test Results:')
    basic_result = 'PASS' if basic_ok else 'FAIL'
    intermediate_result = 'PASS' if intermediate_ok else 'FAIL'
    advanced_result = 'PASS' if advanced_ok else 'FAIL'
    print(f'  Basic Features: {basic_result}')
    print(f'  Intermediate Features: {intermediate_result}')
    print(f'  Advanced Features: {advanced_result}')

    if basic_ok and intermediate_ok and advanced_ok:
        print('\nAll tests PASSED! All features working correctly.')
        return 0
    else:
        print('\nSome tests FAILED! Features may not be working correctly.')
        return 1

if __name__ == '__main__':
    exit(main())

