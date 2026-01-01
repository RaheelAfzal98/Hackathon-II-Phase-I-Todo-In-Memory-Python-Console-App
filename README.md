# The Evolution of Todo - Phase I: In-Memory CLI Todo Application

This project simulates the real-world evolution of software systems. In Phase I, the goal is to design and build a **simple in-memory command-line Todo application** using **spec-driven development** and **AI-assisted coding**.

## Project Overview

Students act as **Product Architects**, focusing on architecture, specifications, and development process rather than writing manual code. The project starts with a basic CLI script and is designed to evolve in later phases into a **distributed, cloud-native, AI-powered system**.

## Features

The application implements all five basic Todo features:

### Add Task
- Create a new todo item
- Required fields:
  - Title
  - Description

### View Task List
- Display all todo items
- Each task shows:
  - Unique ID
  - Title
  - Description
  - Completion status (Complete / Incomplete)

### Update Task
- Modify an existing task using its ID
- Editable fields:
  - Title
  - Description

### Delete Task
- Remove a task permanently using its ID

### Mark Task as Complete
- Toggle task status:
  - Complete
  - Incomplete

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

## Data Constraints

- All data is stored **in memory only**
- No file system persistence
- No databases
- Data is lost when the application exits