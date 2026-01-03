"""Main entry point for the todo CLI application."""

import sys
import argparse
from typing import Optional
from .services import TodoService
from .models import Todo
from .cli import TodoCLI as InteractiveTodoCLI


def run_command_line_interface():
    """Run the command-line interface with arguments."""
    parser = argparse.ArgumentParser(description='Todo CLI Application')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('title', help='Task title')
    add_parser.add_argument('description', help='Task description')
    add_parser.add_argument('--priority', default='medium', choices=['high', 'medium', 'low'], help='Task priority (default: medium)')
    add_parser.add_argument('--tags', nargs='*', default=[], help='Task tags (space-separated)')
    add_parser.add_argument('--due-date', help='Due date in YYYY-MM-DD format')
    add_parser.add_argument('--recurring', action='store_true', help='Make task recurring')
    add_parser.add_argument('--recurrence-pattern', choices=['daily', 'weekly', 'custom'], help='Recurrence pattern')
    add_parser.add_argument('--recurrence-interval', type=int, help='Recurrence interval in days (for custom pattern)')

    # List command
    list_parser = subparsers.add_parser('list', help='List all tasks')
    list_parser.add_argument('--filter-status', choices=['completed', 'incomplete'], help='Filter by completion status')
    list_parser.add_argument('--filter-priority', choices=['high', 'medium', 'low'], help='Filter by priority')
    list_parser.add_argument('--filter-tag', help='Filter by tag')
    list_parser.add_argument('--filter-overdue', action='store_true', help='Filter by overdue status')
    list_parser.add_argument('--filter-recurring', action='store_true', help='Filter by recurring status')
    list_parser.add_argument('--sort', choices=['priority', 'title', 'id'], help='Sort by field')
    list_parser.add_argument('--ascending', action='store_true', help='Sort in ascending order (default: descending)')

    # Update command
    update_parser = subparsers.add_parser('update', help='Update a task')
    update_parser.add_argument('id', help='Task ID')
    update_parser.add_argument('--title', help='New task title')
    update_parser.add_argument('--description', help='New task description')
    update_parser.add_argument('--priority', choices=['high', 'medium', 'low'], help='New task priority')
    update_parser.add_argument('--tags', nargs='*', help='New task tags (space-separated)')
    update_parser.add_argument('--due-date', help='New due date in YYYY-MM-DD format')
    update_parser.add_argument('--clear-due-date', action='store_true', help='Clear the due date')
    update_parser.add_argument('--recurring', choices=['true', 'false'], help='Set recurring status (true/false)')
    update_parser.add_argument('--recurrence-pattern', choices=['daily', 'weekly', 'custom'], help='New recurrence pattern')
    update_parser.add_argument('--recurrence-interval', type=int, help='New recurrence interval in days (for custom pattern)')

    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', help='Task ID')

    # Complete command
    complete_parser = subparsers.add_parser('complete', help='Toggle task completion')
    complete_parser.add_argument('id', help='Task ID')

    # Search command
    search_parser = subparsers.add_parser('search', help='Search tasks by keyword')
    search_parser.add_argument('keyword', help='Keyword to search for in title or description or tags')

    # Parse arguments
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    service = TodoService()

    if args.command == 'add':
        # Process due date
        due_date = None
        if args.due_date:
            try:
                from datetime import datetime
                due_date = datetime.strptime(args.due_date, "%Y-%m-%d")
            except ValueError:
                print(f"Error: Invalid date format for due date: {args.due_date}. Use YYYY-MM-DD format.")
                return

        # Process recurrence parameters
        is_recurring = args.recurring
        recurrence_pattern = args.recurrence_pattern
        recurrence_interval = args.recurrence_interval

        # Validate recurrence parameters
        if is_recurring and not recurrence_pattern:
            recurrence_pattern = "daily"  # Default to daily if recurring but no pattern specified

        try:
            task = service.add_task(
                args.title,
                args.description,
                args.priority,
                args.tags,
                due_date,
                is_recurring,
                recurrence_pattern,
                recurrence_interval
            )
            print(f"Added task: {task.id} - {task.title}")
            print(f"  Priority: {task.priority}")
            if task.tags:
                print(f"  Tags: {', '.join(task.tags)}")
            if task.due_date:
                print(f"  Due Date: {task.due_date.strftime('%Y-%m-%d')}")
            if task.is_recurring:
                recurrence_info = f"  Recurring: {task.recurrence_pattern}"
                if task.recurrence_pattern == "custom" and task.recurrence_interval:
                    recurrence_info += f" every {task.recurrence_interval} days"
                print(recurrence_info)
        except ValueError as e:
            print(f"Error: {e}")
    elif args.command == 'list':
        # Get all tasks first
        tasks = service.list_tasks()

        # Apply filters - each filter narrows down the results
        if args.filter_status:
            tasks = service.filter_by_status(args.filter_status)
        if args.filter_priority:
            tasks = [task for task in tasks if task.priority == args.filter_priority]
        if args.filter_tag:
            tasks = service.filter_by_tag(args.filter_tag)
        if args.filter_overdue:
            tasks = [task for task in tasks if service.is_overdue(task)]
        if args.filter_recurring:
            tasks = [task for task in tasks if task.is_recurring]

        # Apply sorting if requested
        if args.sort:
            tasks = service.sort_tasks(tasks, args.sort, args.ascending)

        if not tasks:
            print("No tasks found.")
            return

        print("Todo List:")
        print("-" * 50)
        for task in tasks:
            status = "[X]" if task.completed else "[ ]"
            # Check if task is overdue
            overdue_indicator = ""
            if service.is_overdue(task):
                overdue_indicator = " [OVERDUE]"
            print(f"{status}{overdue_indicator} {task.id[:8]} - {task.title}")
            print(f"      Full ID: {task.id}")
            print(f"      Priority: {task.priority}")
            if task.due_date:
                print(f"      Due Date: {task.due_date.strftime('%Y-%m-%d %H:%M:%S')}")
            if task.is_recurring:
                recurrence_info = f"      Recurring: {task.recurrence_pattern}"
                if task.recurrence_pattern == "custom" and task.recurrence_interval:
                    recurrence_info += f" every {task.recurrence_interval} days"
                print(recurrence_info)
            if task.tags:
                print(f"      Tags: {', '.join(task.tags)}")
            print(f"      {task.description}")
            print()
    elif args.command == 'update':
        # Check if any update parameters were provided
        has_update_params = any([
            args.title, args.description, args.priority, args.tags,
            args.due_date is not None, args.clear_due_date,
            args.recurring, args.recurrence_pattern, args.recurrence_interval is not None
        ])

        if not has_update_params:
            print("Please provide at least a new title, description, priority, tags, or advanced options")
            return

        # Process due date
        due_date = None
        if args.clear_due_date:
            due_date = None  # Explicitly clear the due date
        elif args.due_date:
            try:
                from datetime import datetime
                due_date = datetime.strptime(args.due_date, "%Y-%m-%d")
            except ValueError:
                print(f"Error: Invalid date format for due date: {args.due_date}. Use YYYY-MM-DD format.")
                return
        else:
            due_date = None  # Don't change existing due date

        # Process recurring status
        is_recurring = None
        if args.recurring == 'true':
            is_recurring = True
        elif args.recurring == 'false':
            is_recurring = False
        # If args.recurring is None, we don't change the existing value

        # Process recurrence pattern and interval
        recurrence_pattern = args.recurrence_pattern
        recurrence_interval = args.recurrence_interval

        updated_task = service.update_task(
            args.id,
            args.title,
            args.description,
            args.priority,
            args.tags,
            due_date,
            is_recurring,
            recurrence_pattern,
            recurrence_interval
        )

        if updated_task:
            print(f"Updated task: {updated_task.id} - {updated_task.title}")
            print(f"  New Priority: {updated_task.priority}")
            if updated_task.tags:
                print(f"  New Tags: {', '.join(updated_task.tags)}")
            if updated_task.due_date:
                print(f"  New Due Date: {updated_task.due_date.strftime('%Y-%m-%d')}")
            elif args.clear_due_date:
                print("  Due Date: Cleared")
            if updated_task.is_recurring:
                recurrence_info = f"  Recurring: {updated_task.recurrence_pattern}"
                if updated_task.recurrence_pattern == "custom" and updated_task.recurrence_interval:
                    recurrence_info += f" every {updated_task.recurrence_interval} days"
                print(recurrence_info)
        else:
            print(f"Task with ID {args.id} not found")
    elif args.command == 'delete':
        success = service.delete_task(args.id)
        if success:
            print(f"Deleted task with ID: {args.id}")
        else:
            print(f"Task with ID {args.id} not found")
    elif args.command == 'complete':
        task = service.toggle_task_completion(args.id)
        if task:
            status = "completed" if task.completed else "incomplete"
            print(f"Task marked as {status}: {task.id} - {task.title}")
        else:
            print(f"Task with ID {args.id} not found")
    elif args.command == 'search':
        results = service.search_tasks(args.keyword)
        if not results:
            print(f"No tasks found matching '{args.keyword}'.")
            return

        print(f"Search results for '{args.keyword}':")
        print("-" * 50)
        for task in results:
            status = "[X]" if task.completed else "[ ]"
            # Check if task is overdue
            overdue_indicator = ""
            if service.is_overdue(task):
                overdue_indicator = " [OVERDUE]"
            print(f"{status}{overdue_indicator} {task.id[:8]} - {task.title}")
            print(f"      Full ID: {task.id}")
            print(f"      Priority: {task.priority}")
            if task.due_date:
                print(f"      Due Date: {task.due_date.strftime('%Y-%m-%d %H:%M:%S')}")
            if task.is_recurring:
                recurrence_info = f"      Recurring: {task.recurrence_pattern}"
                if task.recurrence_pattern == "custom" and task.recurrence_interval:
                    recurrence_info += f" every {task.recurrence_interval} days"
                print(recurrence_info)
            if task.tags:
                print(f"      Tags: {', '.join(task.tags)}")
            print(f"      {task.description}")
            print()


def run_interactive_interface():
    """Run the interactive menu-based interface."""
    cli = InteractiveTodoCLI()
    cli.run()


def main():
    """Main entry point."""
    # Check if command line arguments are provided
    if len(sys.argv) > 1:
        # Use command-line interface
        run_command_line_interface()
    else:
        # Use interactive interface
        run_interactive_interface()


if __name__ == "__main__":
    main()