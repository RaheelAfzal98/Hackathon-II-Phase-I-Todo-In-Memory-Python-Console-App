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

    # List command
    subparsers.add_parser('list', help='List all tasks')

    # Update command
    update_parser = subparsers.add_parser('update', help='Update a task')
    update_parser.add_argument('id', help='Task ID')
    update_parser.add_argument('--title', help='New task title')
    update_parser.add_argument('--description', help='New task description')

    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', help='Task ID')

    # Complete command
    complete_parser = subparsers.add_parser('complete', help='Toggle task completion')
    complete_parser.add_argument('id', help='Task ID')

    # Parse arguments
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    service = TodoService()

    if args.command == 'add':
        try:
            task = service.add_task(args.title, args.description)
            print(f"Added task: {task.id} - {task.title}")
        except ValueError as e:
            print(f"Error: {e}")
    elif args.command == 'list':
        tasks = service.list_tasks()
        if not tasks:
            print("No tasks found.")
            return

        print("Todo List:")
        print("-" * 50)
        for task in tasks:
            status = "[X]" if task.completed else "[ ]"
            print(f"{status} {task.id[:8]} - {task.title}")
            print(f"      Full ID: {task.id}")
            print(f"      {task.description}")
            print()
    elif args.command == 'update':
        if args.title is None and args.description is None:
            print("Please provide at least a new title or description")
            return

        updated_task = service.update_task(args.id, args.title, args.description)
        if updated_task:
            print(f"Updated task: {updated_task.id} - {updated_task.title}")
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