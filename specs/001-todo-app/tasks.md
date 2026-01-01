# Implementation Tasks: In-Memory CLI Todo Application

**Feature**: In-Memory CLI Todo Application
**Branch**: 001-todo-app
**Created**: 2025-12-31
**Input**: Feature specification and implementation plan

## Implementation Strategy

Build the application incrementally following clean architecture principles with separation of concerns. Start with foundational components, then implement user stories in priority order (P1, P2, P3...). Each user story should be independently testable and deliver value.

**MVP Scope**: User Story 1 (Add Todo Task) with minimal supporting infrastructure for a fully functional core.

## Phase 1: Project Setup

**Goal**: Establish project structure and foundational files per implementation plan

- [X] T001 Create src/todo directory structure
- [X] T002 Create empty __init__.py file in src/todo/
- [X] T003 Create models.py file in src/todo/ with basic file structure
- [X] T004 Create services.py file in src/todo/ with basic file structure
- [X] T005 Create cli.py file in src/todo/ with basic file structure
- [X] T006 Create main.py file in src/todo/ with basic file structure
- [X] T007 Create pyproject.toml with project metadata and Python 3.13+ requirement

## Phase 2: Foundational Components

**Goal**: Implement core data models and in-memory storage that all user stories depend on

- [X] T008 [P] Define Todo dataclass in src/todo/models.py with id, title, description, completed fields
- [X] T009 [P] Implement TodoModel class in src/todo/models.py with in-memory storage using dictionary
- [X] T010 [P] Implement add_todo method in TodoModel with UUID generation
- [X] T011 [P] Implement get_all_todos method in TodoModel
- [X] T012 [P] Implement get_todo method in TodoModel
- [X] T013 [P] Implement update_todo method in TodoModel
- [X] T014 [P] Implement delete_todo method in TodoModel
- [X] T015 [P] Implement toggle_completion method in TodoModel

## Phase 3: User Story 1 - Add Todo Task (Priority: P1)

**Goal**: Implement the ability for users to create new todo tasks with title and description

**Independent Test**: Can be fully tested by adding a task and verifying it appears in the task list - delivers core value of task creation.

- [X] T016 [P] [US1] Implement add_task method in TodoService in src/todo/services.py
- [X] T017 [P] [US1] Add input validation to ensure title and description are provided in services layer
- [X] T018 [P] [US1] Implement command-line interface for adding tasks in src/todo/main.py
- [X] T019 [P] [US1] Implement interactive CLI menu option for adding tasks in src/todo/cli.py
- [X] T020 [US1] Test adding a task via command line and verify it's stored correctly

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Implement the ability for users to see all their todo tasks in one place

**Independent Test**: Can be fully tested by viewing the task list after adding tasks - delivers core value of task visibility.

- [X] T021 [P] [US2] Implement list_tasks method in TodoService in src/todo/services.py
- [X] T022 [P] [US2] Implement command-line interface for listing tasks in src/todo/main.py
- [X] T023 [P] [US2] Implement interactive CLI menu option for viewing tasks in src/todo/cli.py
- [X] T024 [US2] Test viewing task list and verify all fields (ID, title, description, status) are displayed

## Phase 5: User Story 5 - Mark Task Complete/Incomplete (Priority: P1)

**Goal**: Implement the ability for users to track which tasks are completed and which still need to be done

**Independent Test**: Can be fully tested by toggling task completion status and verifying the status changes - delivers value of task status tracking.

- [X] T025 [P] [US5] Implement toggle_task_completion method in TodoService in src/todo/services.py
- [X] T026 [P] [US5] Implement command-line interface for toggling completion in src/todo/main.py
- [X] T027 [P] [US5] Implement interactive CLI menu option for toggling completion in src/todo/cli.py
- [X] T028 [US5] Test toggling task completion status and verify it changes correctly

## Phase 6: User Story 3 - Update Task (Priority: P2)

**Goal**: Implement the ability for users to modify an existing task's title or description

**Independent Test**: Can be fully tested by updating a task and verifying changes are reflected - delivers value of task modification.

- [X] T029 [P] [US3] Enhance update_task method in TodoService with proper validation in src/todo/services.py
- [X] T030 [P] [US3] Implement command-line interface for updating tasks in src/todo/main.py
- [X] T031 [P] [US3] Implement interactive CLI menu option for updating tasks in src/todo/cli.py
- [X] T032 [US3] Test updating task title and description and verify changes are saved

## Phase 7: User Story 4 - Delete Task (Priority: P2)

**Goal**: Implement the ability for users to remove completed or unwanted tasks

**Independent Test**: Can be fully tested by deleting a task and verifying it no longer appears in the list - delivers value of task removal.

- [X] T033 [P] [US4] Implement delete_task method in TodoService in src/todo/services.py
- [X] T034 [P] [US4] Implement command-line interface for deleting tasks in src/todo/main.py
- [X] T035 [P] [US4] Implement interactive CLI menu option for deleting tasks in src/todo/cli.py
- [X] T036 [US4] Test deleting a task and verify it's removed from storage

## Phase 8: Polish & Cross-Cutting Concerns

**Goal**: Implement error handling, validation, and finalize the application

- [X] T037 Add error handling for invalid task IDs across all service methods
- [X] T038 Implement proper error messages for all user interactions
- [X] T039 Add input validation to prevent empty titles in all interfaces
- [X] T040 Test all edge cases: invalid IDs, empty inputs, non-existent tasks
- [X] T041 Update README.md with setup and usage instructions
- [X] T042 Test complete user workflows to ensure all features work together
- [X] T043 Perform final integration test of all user stories

## Dependencies

**User Story Order**: All P1 stories (US1, US2, US5) can be developed in parallel or in any order. US3 and US4 depend on the foundational models but can be developed after all P1 stories are complete.

## Parallel Execution Examples

**Per Story**:
- US1: Model implementation (T008-T015) can happen in parallel with service implementation (T016-T017) and CLI implementation (T018-T019)
- US2: Service implementation (T021) can happen in parallel with CLI implementation (T022-T023)
- US3: Service implementation (T029) can happen in parallel with CLI implementation (T030-T031)
- US4: Service implementation (T033) can happen in parallel with CLI implementation (T034-T035)
- US5: Service implementation (T025) can happen in parallel with CLI implementation (T026-T027)