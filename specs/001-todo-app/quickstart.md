# Quickstart: In-Memory CLI Todo Application

## Setup

1. Ensure Python 3.13+ is installed
2. Clone the repository
3. Navigate to the project directory

## Running the Application

### Interactive Mode (Recommended for new users)
```bash
python -m src.todo.main
```

### Command-Line Mode
```bash
# Add a task
python -m src.todo.main add "Task Title" "Task Description"

# List all tasks
python -m src.todo.main list

# Update a task
python -m src.todo.main update <task-id> --title "New Title" --description "New Description"

# Delete a task
python -m src.todo.main delete <task-id>

# Mark task as complete/incomplete
python -m src.todo.main complete <task-id>
```

## Features

1. **Add Task**: Create new todo items with title and description
2. **View Tasks**: See all tasks with ID, title, description, and completion status
3. **Update Task**: Modify existing tasks by ID
4. **Delete Task**: Remove tasks permanently by ID
5. **Toggle Completion**: Mark tasks as complete/incomplete by ID

## Important Notes

- All data is stored in memory only and will be lost when the application exits
- Each task is assigned a unique ID automatically
- Tasks are marked as incomplete by default when created
- The interactive mode provides a menu-driven interface for easier use