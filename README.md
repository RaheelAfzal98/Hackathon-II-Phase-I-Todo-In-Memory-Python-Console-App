# The Evolution of Todo - Phase I: In-Memory CLI Todo Application

This project simulates the real-world evolution of software systems. In Phase I, the goal is to design and build a **simple in-memory command-line Todo application** using **spec-driven development** and **AI-assisted coding**.

## Project Overview

Students act as **Product Architects**, focusing on architecture, specifications, and development process rather than writing manual code. The project starts with a basic CLI script and is designed to evolve in later phases into a **distributed, cloud-native, AI-powered system**.

## Features

The application implements all five basic Todo features plus intermediate features:

### Basic Features

#### Add Task
- Create a new todo item
- Required fields:
  - Title
  - Description

#### View Task List
- Display all todo items
- Each task shows:
  - Unique ID
  - Title
  - Description
  - Completion status (Complete / Incomplete)

#### Update Task
- Modify an existing task using its ID
- Editable fields:
  - Title
  - Description

#### Delete Task
- Remove a task permanently using its ID

#### Mark Task as Complete
- Toggle task status:
  - Complete
  - Incomplete

### Intermediate Features (New in Phase I)

#### Priority and Tags
- Assign priority levels to tasks: high, medium, low
- Add tags to tasks for categorization
- Default priority is "medium" if not specified
- Default tags is an empty list if not specified

#### Search Tasks
- Search for tasks by keyword in title, description, or tags
- Case-insensitive search by default
- Use the `search` command to find matching tasks

#### Filter Tasks
- Filter tasks by completion status (completed/incomplete)
- Filter tasks by priority (high/medium/low)
- Filter tasks by tag
- Combine multiple filters together

#### Sort Tasks
- Sort tasks by priority (high → medium → low)
- Sort tasks alphabetically by title
- Sort tasks by ID
- Choose ascending or descending order

### Advanced Features (New in Phase I)

#### Recurring Tasks
- Create tasks that repeat automatically
- Supported patterns: daily, weekly, custom interval
- When completed, recurring tasks generate the next occurrence automatically
- Recurring behavior can be enabled/disabled for existing tasks
- Custom intervals can be set in days

#### Due Dates & Time Reminders
- Assign optional due dates and times to tasks
- System tracks and identifies overdue tasks
- CLI clearly indicates overdue status in task listings
- Time reminders operate within CLI/runtime constraints

## Technology Stack

- Python **3.13+**
- Command Line Interface (CLI)
- In-memory data storage
- Tools:
  - Spec-Kit Plus
  - Claude Code

## Project Structure

```
/
├── src/
│ └── todo/
│   ├── __init__.py
│   ├── models.py          # Todo data models and in-memory storage
│   ├── services.py        # Business logic layer
│   ├── cli.py             # Interactive CLI interface
│   └── main.py            # Application entry point
├── tests/
├── README.md
├── CLAUDE.md
├── pyproject.toml
└── .gitignore
```

## Setup Instructions

1. Ensure Python 3.13+ is installed on your system
2. Clone this repository
3. Navigate to the project directory

## Usage

### Interactive Mode (Recommended for new users)
```bash
python -m src.todo.main
```

### Command-Line Mode
```bash
# Add a task with priority and tags
python -m src.todo.main add "Task Title" "Task Description" --priority high --tags work urgent

# Add a task with due date
python -m src.todo.main add "Task Title" "Task Description" --due-date 2026-12-31

# Add a recurring task (daily)
python -m src.todo.main add "Daily Task" "Description" --recurring --recurrence-pattern daily

# Add a recurring task (weekly)
python -m src.todo.main add "Weekly Task" "Description" --recurring --recurrence-pattern weekly

# Add a recurring task (custom interval)
python -m src.todo.main add "Custom Task" "Description" --recurring --recurrence-pattern custom --recurrence-interval 5

# List all tasks
python -m src.todo.main list

# List tasks with filters
python -m src.todo.main list --filter-status completed
python -m src.todo.main list --filter-priority high
python -m src.todo.main list --filter-tag work
python -m src.todo.main list --filter-status incomplete --filter-priority high

# List tasks with advanced filters
python -m src.todo.main list --filter-overdue
python -m src.todo.main list --filter-recurring
python -m src.todo.main list --filter-status incomplete --filter-overdue

# List tasks with sorting
python -m src.todo.main list --sort priority
python -m src.todo.main list --sort title --ascending
python -m src.todo.main list --sort priority --ascending

# Update a task with priority and tags
python -m src.todo.main update <task-id> --title "New Title" --description "New Description" --priority low --tags personal

# Update a task with due date
python -m src.todo.main update <task-id> --due-date 2026-12-31

# Update a task to clear due date
python -m src.todo.main update <task-id> --clear-due-date

# Update a task to make it recurring
python -m src.todo.main update <task-id> --recurring true --recurrence-pattern weekly

# Update a task to disable recurring
python -m src.todo.main update <task-id> --recurring false

# Delete a task
python -m src.todo.main delete <task-id>

# Mark task as complete/incomplete
python -m src.todo.main complete <task-id>

# Search tasks by keyword
python -m src.todo.main search "keyword"
```

## Data Constraints

- All data is stored **in memory only**
- No file system persistence
- No databases
- Data is lost when the application exits