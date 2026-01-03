# Implementation Tasks: Advanced Todo Features

**Feature**: Advanced Todo Features (Recurring Tasks & Due Dates)
**Branch**: 001-advanced-todo-features
**Spec**: [spec.md](./spec.md) | **Plan**: [plan.md](./plan.md)
**Generated**: 2026-01-03

## Implementation Strategy

**MVP Scope**: User Story 1 (Create Recurring Tasks) - This delivers the core value of recurring tasks functionality.

**Approach**: Implement features incrementally following user story priorities:
- P1: Create Recurring Tasks, Complete Recurring Tasks
- P2: Set Due Dates and Time Reminders, Manage Recurring Task Patterns
- P3: Handle Overdue Recurring Tasks

## Dependencies

- **User Story 2** depends on **User Story 1** (need to create recurring tasks before completing them)
- **User Story 5** depends on **User Story 1 & 2** (handles overdue recurring tasks)

## Parallel Execution Examples

- **US1 (P1)**: Model enhancements can run in parallel with CLI updates
- **US3 (P2)**: Due date model changes can run in parallel with service layer updates
- **US4 (P2)**: Update functionality can run in parallel with CLI display updates

## Phase 1: Setup Tasks

### Goal: Prepare project structure for advanced features implementation

- [ ] T001 Set up development environment with Python 3.13
- [ ] T002 Verify existing Basic and Intermediate features work correctly
- [ ] T003 Create backup of current working codebase

## Phase 2: Foundational Tasks

### Goal: Implement core data structures and validation for advanced features

- [ ] T010 [P] Extend Todo model with due_date field in src/todo/models.py
- [ ] T011 [P] Extend Todo model with recurrence fields (is_recurring, recurrence_pattern, recurrence_interval) in src/todo/models.py
- [ ] T012 [P] Add validation rules for recurrence fields in src/todo/models.py
- [ ] T013 [P] Add datetime import to models.py for due date handling
- [ ] T014 [P] Update TodoModel methods to handle new fields in src/todo/models.py
- [ ] T015 [P] Implement generate_next_occurrence method in TodoModel in src/todo/models.py
- [ ] T016 [P] Add overdue checking logic to models in src/todo/models.py

## Phase 3: User Story 1 - Create Recurring Tasks (Priority: P1)

### Goal: Enable users to create recurring tasks with daily, weekly, and custom interval patterns

**Independent Test Criteria**: Can be fully tested by creating a daily recurring task and verifying that it appears in the task list. Delivers value by reducing repetitive task creation.

**Acceptance Scenarios**:
1. Given user is in the CLI application, When user creates a recurring task with daily pattern, Then the task appears in the list and is marked as recurring
2. Given user has created a recurring task, When user views the task list, Then recurring tasks are clearly identified with their recurrence pattern

- [ ] T020 [US1] Update TodoService.add_task to accept recurrence parameters in src/todo/services.py
- [ ] T021 [US1] Add recurrence validation to add_task method in src/todo/services.py
- [ ] T022 [US1] Update CLI add_task_ui to accept recurrence options in src/todo/cli.py
- [ ] T023 [US1] Add recurrence pattern selection (daily/weekly/custom) to CLI in src/todo/cli.py
- [ ] T024 [US1] Update main.py CLI command to accept recurrence parameters in src/todo/main.py
- [ ] T025 [US1] Update main.py add command to include recurrence options in src/todo/main.py
- [ ] T026 [US1] Update task display to show recurrence information in src/todo/cli.py
- [ ] T027 [US1] Update task display in main.py list command to show recurrence info in src/todo/main.py
- [ ] T028 [US1] Test creating recurring tasks with different patterns

## Phase 4: User Story 2 - Complete Recurring Tasks (Priority: P1)

### Goal: When a recurring task is completed, automatically generate the next occurrence

**Independent Test Criteria**: Can be fully tested by completing a recurring task and verifying that a new occurrence is created. Delivers value by maintaining the user's routine automatically.

**Acceptance Scenarios**:
1. Given user has a daily recurring task, When user marks it complete, Then the current occurrence is marked complete and a new occurrence is scheduled for the next day
2. Given user has a recurring task with due date, When user completes it, Then the new occurrence inherits the same recurrence pattern and timing

- [ ] T030 [US2] Update TodoModel.toggle_completion to handle recurring tasks in src/todo/models.py
- [ ] T031 [US2] Implement generate_next_occurrence logic for different patterns in src/todo/models.py
- [ ] T032 [US2] Update TodoService.toggle_task_completion to handle recurrence in src/todo/services.py
- [ ] T033 [US2] Update CLI toggle_completion_ui to handle recurring tasks in src/todo/cli.py
- [ ] T034 [US2] Update main.py complete command to handle recurrence in src/todo/main.py
- [ ] T035 [US2] Test completing recurring tasks and verifying next occurrence creation
- [ ] T036 [US2] Verify new occurrence has correct due date based on pattern

## Phase 5: User Story 3 - Set Due Dates and Time Reminders (Priority: P2)

### Goal: Enable users to assign due dates and times to tasks and track overdue status

**Independent Test Criteria**: Can be fully tested by creating a task with a due date and checking that it shows the due date. Delivers value by providing time-aware task management.

**Acceptance Scenarios**:
1. Given user is in the CLI application, When user creates a task with a due date, Then the due date is stored and displayed with the task
2. Given a task has passed its due date, When user views the task list, Then the task is clearly marked as overdue

- [ ] T040 [US3] Update TodoService.add_task to accept due_date parameter in src/todo/services.py
- [ ] T041 [US3] Update TodoService.update_task to accept due_date parameter in src/todo/services.py
- [ ] T042 [US3] Add is_overdue method to TodoService in src/todo/services.py
- [ ] T043 [US3] Add get_overdue_tasks method to TodoService in src/todo/services.py
- [ ] T044 [US3] Update CLI add_task_ui to accept due date in src/todo/cli.py
- [ ] T045 [US3] Update CLI update_task_ui to accept due date in src/todo/cli.py
- [ ] T046 [US3] Update CLI view_tasks_ui to show overdue status in src/todo/cli.py
- [ ] T047 [US3] Update main.py add command to accept due_date parameter in src/todo/main.py
- [ ] T048 [US3] Update main.py update command to accept due_date parameter in src/todo/main.py
- [ ] T049 [US3] Update main.py list command to show overdue status in src/todo/main.py
- [ ] T050 [US3] Add overdue indicators to task display formats in src/todo/cli.py and src/todo/main.py
- [ ] T051 [US3] Test due date creation and overdue status display

## Phase 6: User Story 4 - Manage Recurring Task Patterns (Priority: P2)

### Goal: Allow users to edit existing recurring tasks to change their recurrence patterns

**Independent Test Criteria**: Can be fully tested by creating a recurring task and then updating its recurrence pattern. Delivers value by allowing users to adjust their recurring tasks.

**Acceptance Scenarios**:
1. Given user has a recurring task, When user updates the recurrence pattern, Then future occurrences follow the new pattern

- [ ] T055 [US4] Update TodoService.update_task to modify recurrence parameters in src/todo/services.py
- [ ] T056 [US4] Add validation for changing recurrence patterns in src/todo/services.py
- [ ] T057 [US4] Update CLI update_task_ui to modify recurrence options in src/todo/cli.py
- [ ] T058 [US4] Update main.py update command to accept recurrence parameters in src/todo/main.py
- [ ] T059 [US4] Test updating recurrence patterns for existing tasks
- [ ] T060 [US4] Verify future occurrences follow new pattern after update

## Phase 7: User Story 5 - Handle Overdue Recurring Tasks (Priority: P3)

### Goal: Ensure overdue recurring tasks don't skip occurrences silently

**Independent Test Criteria**: Can be fully tested by allowing a recurring task to become overdue and then completing it, verifying the next occurrence is scheduled correctly. Delivers value by maintaining task integrity.

**Acceptance Scenarios**:
1. Given a recurring task is overdue, When user completes it, Then the next occurrence is scheduled from the current date

- [ ] T065 [US5] Update recurring task completion logic to handle overdue cases in src/todo/models.py
- [ ] T066 [US5] Modify generate_next_occurrence to consider current date for overdue tasks in src/todo/models.py
- [ ] T067 [US5] Test overdue recurring task completion behavior
- [ ] T068 [US5] Verify next occurrence is properly scheduled after completing overdue recurring task

## Phase 8: Polish & Cross-Cutting Concerns

### Goal: Ensure all features work together and maintain backward compatibility

- [ ] T070 Update README.md with new CLI commands for advanced features
- [ ] T071 Test backward compatibility with existing Basic and Intermediate features
- [ ] T072 Verify no regressions in existing functionality
- [ ] T073 Add error handling for invalid recurrence patterns
- [ ] T074 Add error handling for invalid due dates
- [ ] T075 Test edge cases from specification (invalid intervals, multiple completions, etc.)
- [ ] T076 Perform integration testing of all advanced features together
- [ ] T077 Verify all CLI commands work correctly with new features
- [ ] T078 Update help text and documentation for new commands
- [ ] T079 Run full test suite to ensure no breaking changes
- [ ] T080 Final validation that all success criteria from spec are met