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
        print("6. Search Tasks")
        print("7. Filter Tasks")
        print("8. Sort Tasks")
        print("9. Exit")
        print("="*40)

    def get_user_choice(self) -> str:
        """Get user's menu choice."""
        choice = input("Enter your choice (1-9): ").strip()
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

        # Get priority
        priority = input("Enter priority (high/medium/low, default: medium): ").strip().lower()
        if priority not in ["high", "medium", "low"]:
            priority = "medium"

        # Get tags
        tags_input = input("Enter tags (comma-separated, optional): ").strip()
        tags = []
        if tags_input:
            tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]

        # Get due date
        due_date_input = input("Enter due date (YYYY-MM-DD, optional): ").strip()
        due_date = None
        if due_date_input:
            try:
                from datetime import datetime
                due_date = datetime.strptime(due_date_input, "%Y-%m-%d")
            except ValueError:
                print(f"Invalid date format for due date: {due_date_input}. Using no due date.")
                due_date = None

        # Get recurrence options
        is_recurring_input = input("Is this a recurring task? (y/n, default: n): ").strip().lower()
        is_recurring = is_recurring_input in ['y', 'yes']

        recurrence_pattern = None
        recurrence_interval = None
        if is_recurring:
            print("Select recurrence pattern:")
            print("1. Daily")
            print("2. Weekly")
            print("3. Custom interval")
            recurrence_choice = input("Enter your choice (1-3, default: 1): ").strip()

            if recurrence_choice == '2':
                recurrence_pattern = "weekly"
            elif recurrence_choice == '3':
                recurrence_pattern = "custom"
                try:
                    recurrence_interval = int(input("Enter interval in days: ").strip())
                    if recurrence_interval <= 0:
                        print("Invalid interval. Using daily recurrence.")
                        recurrence_pattern = "daily"
                        recurrence_interval = None
                except ValueError:
                    print("Invalid interval. Using daily recurrence.")
                    recurrence_pattern = "daily"
                    recurrence_interval = None
            else:  # Default to daily
                recurrence_pattern = "daily"

        try:
            task = self.service.add_task(title, description, priority, tags, due_date, is_recurring, recurrence_pattern, recurrence_interval)
            print(f"+ Added task: {task.title}")
            print(f"  Priority: {task.priority}")
            if task.tags:
                print(f"  Tags: {', '.join(task.tags)}")
            if task.due_date:
                print(f"  Due date: {task.due_date.strftime('%Y-%m-%d')}")
            if task.is_recurring:
                print(f"  Recurring: {task.recurrence_pattern}" + (f" every {task.recurrence_interval} days" if task.recurrence_pattern == "custom" else ""))
        except ValueError as e:
            print(f"- Error: {e}")

    def view_tasks_ui(self):
        """Handle viewing all tasks."""
        print("\n--- All Tasks ---")
        tasks = self.service.list_tasks()

        if not tasks:
            print("No tasks found.")
            return

        for i, task in enumerate(tasks, 1):
            status = "[X] Completed" if task.completed else "[ ] Incomplete"
            # Check if task is overdue
            overdue_indicator = ""
            if self.service.is_overdue(task):
                overdue_indicator = " [OVERDUE]"
            print(f"{i}. {status}{overdue_indicator} {task.id[:8]} - {task.title}")
            print(f"   Full ID: {task.id}")
            print(f"   Priority: {task.priority}")
            if task.due_date:
                print(f"   Due Date: {task.due_date.strftime('%Y-%m-%d %H:%M:%S')}")
            if task.is_recurring:
                recurrence_info = f"   Recurring: {task.recurrence_pattern}"
                if task.recurrence_pattern == "custom" and task.recurrence_interval:
                    recurrence_info += f" every {task.recurrence_interval} days"
                print(recurrence_info)
            if task.tags:
                print(f"   Tags: {', '.join(task.tags)}")
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

        # Get new priority
        current_priority = existing_task.priority
        new_priority = input(f"Enter new priority (high/medium/low, current: '{current_priority}', press Enter to keep current): ").strip().lower()
        if not new_priority:
            new_priority = current_priority
        elif new_priority not in ["high", "medium", "low"]:
            print(f"Invalid priority value. Keeping current priority: {current_priority}")
            new_priority = current_priority

        # Get new tags
        current_tags = existing_task.tags
        tags_input = input(f"Enter new tags (comma-separated, current: '{', '.join(current_tags)}', press Enter to keep current): ").strip()
        if tags_input:
            new_tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
        else:
            new_tags = current_tags

        # Get new due date
        current_due_date = existing_task.due_date.strftime('%Y-%m-%d') if existing_task.due_date else 'None'
        due_date_input = input(f"Enter new due date (YYYY-MM-DD, current: '{current_due_date}', press Enter to keep current): ").strip()
        new_due_date = existing_task.due_date  # Default to current
        if due_date_input:
            try:
                from datetime import datetime
                new_due_date = datetime.strptime(due_date_input, "%Y-%m-%d")
            except ValueError:
                print(f"Invalid date format: {due_date_input}. Keeping current due date.")
                new_due_date = existing_task.due_date
        elif due_date_input == "":  # User pressed Enter to clear due date
            new_due_date = None

        # Get new recurrence options
        current_recurrence = f"{existing_task.recurrence_pattern}" + (f" every {existing_task.recurrence_interval} days" if existing_task.recurrence_pattern == "custom" and existing_task.recurrence_interval else "")
        current_recurrence_str = f"{current_recurrence}" if existing_task.is_recurring else "None"
        is_recurring_input = input(f"Is recurring? (y/n, current: {'y' if existing_task.is_recurring else 'n'}, press Enter to keep current): ").strip().lower()
        new_is_recurring = existing_task.is_recurring
        new_recurrence_pattern = existing_task.recurrence_pattern
        new_recurrence_interval = existing_task.recurrence_interval

        if is_recurring_input == 'y' or is_recurring_input == 'yes':
            new_is_recurring = True
            print("Select recurrence pattern:")
            print("1. Daily")
            print("2. Weekly")
            print("3. Custom interval")
            recurrence_choice = input(f"Enter your choice (1-3, current: 1 if daily, 2 if weekly, 3 if custom, default: keep current): ").strip()

            if recurrence_choice == '2':
                new_recurrence_pattern = "weekly"
                new_recurrence_interval = None
            elif recurrence_choice == '3':
                new_recurrence_pattern = "custom"
                try:
                    new_recurrence_interval = int(input(f"Enter interval in days (current: {existing_task.recurrence_interval or 'None'}): ").strip())
                    if new_recurrence_interval <= 0:
                        print("Invalid interval. Keeping current recurrence settings.")
                        new_recurrence_pattern = existing_task.recurrence_pattern
                        new_recurrence_interval = existing_task.recurrence_interval
                except ValueError:
                    print("Invalid interval. Keeping current recurrence settings.")
                    new_recurrence_pattern = existing_task.recurrence_pattern
                    new_recurrence_interval = existing_task.recurrence_interval
            elif recurrence_choice == '1':
                new_recurrence_pattern = "daily"
                new_recurrence_interval = None
            else:  # Keep current
                new_recurrence_pattern = existing_task.recurrence_pattern
                new_recurrence_interval = existing_task.recurrence_interval
        elif is_recurring_input == 'n' or is_recurring_input == 'no':
            new_is_recurring = False
            new_recurrence_pattern = None
            new_recurrence_interval = None

        # Use existing values if user didn't provide new ones
        title = new_title if new_title else existing_task.title
        description = new_description if new_description else existing_task.description

        updated_task = self.service.update_task(task_id, title, description, new_priority, new_tags,
                                               new_due_date, new_is_recurring, new_recurrence_pattern, new_recurrence_interval)
        if updated_task:
            print(f"+ Updated task: {updated_task.title}")
            print(f"  New Priority: {updated_task.priority}")
            if updated_task.tags:
                print(f"  New Tags: {', '.join(updated_task.tags)}")
            if updated_task.due_date:
                print(f"  New Due Date: {updated_task.due_date.strftime('%Y-%m-%d')}")
            elif updated_task.due_date is None and existing_task.due_date is not None:
                print("  Due Date: Cleared")
            if updated_task.is_recurring:
                recurrence_info = f"  Recurring: {updated_task.recurrence_pattern}"
                if updated_task.recurrence_pattern == "custom" and updated_task.recurrence_interval:
                    recurrence_info += f" every {updated_task.recurrence_interval} days"
                print(recurrence_info)
            elif updated_task.is_recurring != existing_task.is_recurring and not updated_task.is_recurring:
                print("  Recurring: Disabled")
        else:
            print(f"- Failed to update task with ID {task_id}")

    def delete_task_ui(self):
        """Handle deleting a task."""
        print("\n--- Delete Task ---")
        task_id = input("Enter task ID to delete: ").strip()

        success = self.service.delete_task(task_id)
        if success:
            print(f"+ Deleted task with ID {task_id}")
        else:
            print(f"- Task with ID {task_id} not found")

    def toggle_completion_ui(self):
        """Handle toggling task completion."""
        print("\n--- Toggle Task Completion ---")
        task_id = input("Enter task ID to toggle: ").strip()

        task = self.service.toggle_task_completion(task_id)
        if task:
            status = "completed" if task.completed else "incomplete"
            print(f"+ Task marked as {status}: {task.title}")
        else:
            print(f"- Task with ID {task_id} not found")

    def search_tasks_ui(self):
        """Handle searching tasks by keyword."""
        print("\n--- Search Tasks ---")
        keyword = input("Enter keyword to search: ").strip()

        if not keyword:
            print("Keyword is required!")
            return

        tasks = self.service.search_tasks(keyword)

        if not tasks:
            print("No tasks found matching your search.")
            return

        print(f"\n--- Search Results for '{keyword}' ---")
        for i, task in enumerate(tasks, 1):
            status = "[X] Completed" if task.completed else "[ ] Incomplete"
            print(f"{i}. {status} {task.id[:8]} - {task.title}")
            print(f"   Priority: {task.priority}")
            if task.tags:
                print(f"   Tags: {', '.join(task.tags)}")
            print(f"   {task.description}")
            print()

    def filter_tasks_ui(self):
        """Handle filtering tasks by various criteria."""
        print("\n--- Filter Tasks ---")
        print("Select filter criteria:")
        print("1. By Status (completed/incomplete)")
        print("2. By Priority (high/medium/low)")
        print("3. By Tag")
        print("4. By Overdue Status")
        print("5. By Recurrence")
        print("6. Combined filters")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            status = input("Enter status (completed/incomplete): ").strip().lower()
            if status not in ["completed", "incomplete"]:
                print("Invalid status. Use 'completed' or 'incomplete'.")
                return

            tasks = self.service.filter_by_status(status)

        elif choice == '2':
            priority = input("Enter priority (high/medium/low): ").strip().lower()
            if priority not in ["high", "medium", "low"]:
                print("Invalid priority. Use 'high', 'medium', or 'low'.")
                return

            tasks = self.service.filter_by_priority(priority)

        elif choice == '3':
            tag = input("Enter tag to filter by: ").strip()
            if not tag:
                print("Tag is required!")
                return

            tasks = self.service.filter_by_tag(tag)

        elif choice == '4':
            overdue_choice = input("Show overdue tasks? (y/n): ").strip().lower()
            if overdue_choice in ['y', 'yes']:
                tasks = self.service.get_overdue_tasks()
            else:
                all_tasks = self.service.list_tasks()
                tasks = [task for task in all_tasks if not self.service.is_overdue(task)]

        elif choice == '5':
            recurring_choice = input("Show recurring tasks? (y/n): ").strip().lower()
            if recurring_choice in ['y', 'yes']:
                all_tasks = self.service.list_tasks()
                tasks = [task for task in all_tasks if task.is_recurring]
            else:
                all_tasks = self.service.list_tasks()
                tasks = [task for task in all_tasks if not task.is_recurring]

        elif choice == '6':
            status = input("Enter status (completed/incomplete, press Enter to skip): ").strip().lower()
            if status and status not in ["completed", "incomplete"]:
                print("Invalid status. Use 'completed' or 'incomplete'.")
                return

            priority = input("Enter priority (high/medium/low, press Enter to skip): ").strip().lower()
            if priority and priority not in ["high", "medium", "low"]:
                print("Invalid priority. Use 'high', 'medium', or 'low'.")
                return

            tag = input("Enter tag (press Enter to skip): ").strip()

            tasks = self.service.combine_filters(
                status=status if status else None,
                priority=priority if priority else None,
                tag=tag if tag else None
            )

            # Additional filters for advanced features
            overdue_filter = input("Filter by overdue status? (y/n, press Enter to skip): ").strip().lower()
            if overdue_filter in ['y', 'yes']:
                is_overdue = input("Show only overdue? (y/n): ").strip().lower()
                if is_overdue in ['y', 'yes']:
                    tasks = [task for task in tasks if self.service.is_overdue(task)]
                else:
                    tasks = [task for task in tasks if not self.service.is_overdue(task)]

            recurring_filter = input("Filter by recurrence? (y/n, press Enter to skip): ").strip().lower()
            if recurring_filter in ['y', 'yes']:
                is_recurring = input("Show only recurring? (y/n): ").strip().lower()
                if is_recurring in ['y', 'yes']:
                    tasks = [task for task in tasks if task.is_recurring]
                else:
                    tasks = [task for task in tasks if not task.is_recurring]

        else:
            print("Invalid choice.")
            return

        if not tasks:
            print("No tasks found matching your filter criteria.")
            return

        print("\n--- Filter Results ---")
        for i, task in enumerate(tasks, 1):
            status = "[X] Completed" if task.completed else "[ ] Incomplete"
            # Check if task is overdue
            overdue_indicator = ""
            if self.service.is_overdue(task):
                overdue_indicator = " [OVERDUE]"
            print(f"{i}. {status}{overdue_indicator} {task.id[:8]} - {task.title}")
            print(f"   Priority: {task.priority}")
            if task.due_date:
                print(f"   Due Date: {task.due_date.strftime('%Y-%m-%d %H:%M:%S')}")
            if task.is_recurring:
                recurrence_info = f"   Recurring: {task.recurrence_pattern}"
                if task.recurrence_pattern == "custom" and task.recurrence_interval:
                    recurrence_info += f" every {task.recurrence_interval} days"
                print(recurrence_info)
            if task.tags:
                print(f"   Tags: {', '.join(task.tags)}")
            print(f"   {task.description}")
            print()

    def sort_tasks_ui(self):
        """Handle sorting tasks."""
        print("\n--- Sort Tasks ---")
        print("Select sort field:")
        print("1. Priority (high to low)")
        print("2. Title (alphabetical)")
        print("3. ID")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            sort_field = "priority"
        elif choice == '2':
            sort_field = "title"
        elif choice == '3':
            sort_field = "id"
        else:
            print("Invalid choice.")
            return

        direction = input("Sort ascending? (y/n, default: y): ").strip().lower()
        ascending = direction in ['y', 'yes', '']

        # Get all tasks and sort them
        all_tasks = self.service.list_tasks()
        sorted_tasks = self.service.sort_tasks(all_tasks, sort_field, ascending)

        if not sorted_tasks:
            print("No tasks to display.")
            return

        print(f"\n--- Sorted Tasks ({'ascending' if ascending else 'descending'}) ---")
        for i, task in enumerate(sorted_tasks, 1):
            status = "[X] Completed" if task.completed else "[ ] Incomplete"
            print(f"{i}. {status} {task.id[:8]} - {task.title}")
            print(f"   Priority: {task.priority}")
            if task.tags:
                print(f"   Tags: {', '.join(task.tags)}")
            print(f"   {task.description}")
            print()

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
                self.search_tasks_ui()
            elif choice == '7':
                self.filter_tasks_ui()
            elif choice == '8':
                self.sort_tasks_ui()
            elif choice == '9':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1-9.")

            input("\nPress Enter to continue...")