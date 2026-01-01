"""CLI interaction layer for the todo application."""

from typing import Optional
from .services import TodoService
from .models import Todo


class TodoCLI:
    """Command-line interface for the todo application."""

    def __init__(self):
        """Initialize the CLI with a todo service."""
        self.service = TodoService()

    def display_menu(self):
        """Display the main menu."""
        print("\n" + "="*40)
        print("TODO APPLICATION")
        print("="*40)
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete/Incomplete")
        print("6. Exit")
        print("="*40)

    def get_user_choice(self) -> str:
        """Get user's menu choice."""
        choice = input("Enter your choice (1-6): ").strip()
        return choice

    def add_task_ui(self):
        """Handle adding a new task."""
        print("\n--- Add New Task ---")
        title = input("Enter task title: ").strip()

        if not title:
            print("Title is required!")
            return

        description = input("Enter task description: ").strip()
        if not description:
            description = "No description provided"

        try:
            task = self.service.add_task(title, description)
            print(f"✓ Added task: {task.title}")
        except ValueError as e:
            print(f"✗ Error: {e}")

    def view_tasks_ui(self):
        """Handle viewing all tasks."""
        print("\n--- All Tasks ---")
        tasks = self.service.list_tasks()

        if not tasks:
            print("No tasks found.")
            return

        for i, task in enumerate(tasks, 1):
            status = "[X] Completed" if task.completed else "[ ] Incomplete"
            print(f"{i}. {status} {task.id[:8]} - {task.title}")
            print(f"   Full ID: {task.id}")
            print(f"   {task.description}")
            print()

    def update_task_ui(self):
        """Handle updating a task."""
        print("\n--- Update Task ---")
        task_id = input("Enter task ID to update: ").strip()

        # Check if task exists
        existing_task = self.service.get_task(task_id)
        if not existing_task:
            print(f"Task with ID {task_id} not found.")
            return

        print(f"Current task: {existing_task.title}")
        new_title = input(f"Enter new title (current: '{existing_task.title}', press Enter to keep current): ").strip()
        new_description = input(f"Enter new description (current: '{existing_task.description}', press Enter to keep current): ").strip()

        # Use existing values if user didn't provide new ones
        title = new_title if new_title else existing_task.title
        description = new_description if new_description else existing_task.description

        updated_task = self.service.update_task(task_id, title, description)
        if updated_task:
            print(f"✓ Updated task: {updated_task.title}")
        else:
            print(f"✗ Failed to update task with ID {task_id}")

    def delete_task_ui(self):
        """Handle deleting a task."""
        print("\n--- Delete Task ---")
        task_id = input("Enter task ID to delete: ").strip()

        success = self.service.delete_task(task_id)
        if success:
            print(f"✓ Deleted task with ID {task_id}")
        else:
            print(f"✗ Task with ID {task_id} not found")

    def toggle_completion_ui(self):
        """Handle toggling task completion."""
        print("\n--- Toggle Task Completion ---")
        task_id = input("Enter task ID to toggle: ").strip()

        task = self.service.toggle_task_completion(task_id)
        if task:
            status = "completed" if task.completed else "incomplete"
            print(f"✓ Task marked as {status}: {task.title}")
        else:
            print(f"✗ Task with ID {task_id} not found")

    def run(self):
        """Run the interactive CLI application."""
        print("Welcome to the Todo CLI Application!")

        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == '1':
                self.add_task_ui()
            elif choice == '2':
                self.view_tasks_ui()
            elif choice == '3':
                self.update_task_ui()
            elif choice == '4':
                self.delete_task_ui()
            elif choice == '5':
                self.toggle_completion_ui()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1-6.")

            input("\nPress Enter to continue...")