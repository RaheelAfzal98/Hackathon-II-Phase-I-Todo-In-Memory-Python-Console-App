# Implementation Tasks: Intermediate Level Features for Phase I CLI Todo App

**Feature**: Intermediate Level Features (Priorities & Tags, Search & Filter, Sort Tasks)
**Branch**: 001-intermediate-features
**Input**: Feature specification from `/specs/001-intermediate-features/spec.md`

## Phase 1: Setup

### Goal
Initialize project structure and ensure basic CLI functionality works before implementing new features.

### Independent Test Criteria
- Basic CLI commands (add, list, update, delete, complete) work as before
- Project structure matches specification

### Tasks
- [ ] T001 Create src/todo directory structure if it doesn't exist
- [ ] T002 Create src/todo/__init__.py file
- [ ] T003 Create src/todo/models.py file with basic TodoItem class structure
- [ ] T004 Create src/todo/services.py file with basic service structure
- [ ] T005 Create src/todo/cli.py file with basic CLI structure
- [ ] T006 Create src/todo/main.py file with basic entry point
- [ ] T007 Verify existing basic CLI functionality still works

## Phase 2: Foundational Tasks

### Goal
Implement the core data model extensions and service layer foundations that all user stories depend on.

### Independent Test Criteria
- TodoItem model supports priority and tags fields
- Basic task creation and retrieval works with new fields
- Backward compatibility with existing tasks maintained

### Tasks
- [X] T008 [P] Update TodoItem model in src/todo/models.py to include priority field
- [X] T009 [P] Update TodoItem model in src/todo/models.py to include tags field
- [X] T010 [P] Add validation for priority field ("high", "medium", "low") in models.py
- [X] T011 [P] Add validation for tags field (list of strings) in models.py
- [X] T012 [P] Ensure default values for new fields (priority="medium", tags=[])
- [X] T013 Update TaskCollection to support new TodoItem fields
- [X] T014 [P] Create unit tests for TodoItem model with new fields
- [X] T015 [P] Create unit tests for TaskCollection with new model

## Phase 3: User Story 1 - Add Priority and Tags to Tasks (P1)

### Goal
Enable users to assign priority levels and tags to their tasks during creation and update operations.

### Independent Test Criteria
- Users can create tasks with priority and tags
- Users can update existing tasks to add or modify priority and tags
- Tasks without priority/tags work as before (backward compatibility)

### Tasks
- [X] T016 [US1] Update create_task function in services.py to accept priority parameter
- [X] T017 [US1] Update create_task function in services.py to accept tags parameter
- [X] T018 [US1] Update update_task function in services.py to modify priority
- [X] T019 [US1] Update update_task function in services.py to modify tags
- [X] T020 [US1] Add CLI flags for priority (--priority) to the add command
- [X] T021 [US1] Add CLI flags for tags (--tags) to the add command
- [X] T022 [US1] Add CLI command for updating priority of existing tasks
- [X] T023 [US1] Add CLI command for updating tags of existing tasks
- [X] T024 [US1] Update task display to show priority and tags
- [X] T025 [US1] Test creating tasks with priority and tags
- [X] T026 [US1] Test updating priority and tags of existing tasks
- [X] T027 [US1] Test backward compatibility with tasks without priority/tags

## Phase 4: User Story 2 - Search and Filter Tasks (P1)

### Goal
Enable users to search tasks by keyword and filter tasks by various criteria (status, priority, tags).

### Independent Test Criteria
- Users can search tasks by keyword in title or description
- Users can filter tasks by completion status
- Users can filter tasks by priority level
- Users can filter tasks by tag
- Multiple filters can be combined

### Tasks
- [X] T028 [US2] Implement search_tasks function in services.py for keyword search
- [X] T029 [US2] Implement filter_by_status function in services.py
- [X] T030 [US2] Implement filter_by_priority function in services.py
- [X] T031 [US2] Implement filter_by_tag function in services.py
- [X] T032 [US2] Implement function to combine multiple filters in services.py
- [X] T033 [US2] Add search CLI command with keyword parameter
- [X] T034 [US2] Add filter options (--filter-status) to list command
- [X] T035 [US2] Add filter options (--filter-priority) to list command
- [X] T036 [US2] Add filter options (--filter-tag) to list command
- [X] T037 [US2] Implement support for multiple filter options together
- [X] T038 [US2] Test keyword search functionality
- [X] T039 [US2] Test filtering by status
- [X] T040 [US2] Test filtering by priority
- [X] T041 [US2] Test filtering by tag
- [X] T042 [US2] Test combining multiple filters

## Phase 5: User Story 3 - Sort Tasks by Priority and Alphabetically (P2)

### Goal
Enable users to sort their task list by priority or alphabetically by title without modifying the underlying data.

### Independent Test Criteria
- Users can sort tasks by priority (high → medium → low)
- Users can sort tasks alphabetically by title
- Sorting does not modify the original task list
- Sort operations can be combined with filters

### Tasks
- [X] T043 [US3] Implement sort_tasks function in services.py
- [X] T044 [US3] Implement priority sort logic (high → medium → low)
- [X] T045 [US3] Implement alphabetical sort logic by title
- [X] T046 [US3] Add sort option (--sort) to list command
- [X] T047 [US3] Add sort direction option (--ascending/--descending) to list command
- [X] T048 [US3] Ensure sorting does not mutate original data
- [X] T049 [US3] Test sorting by priority
- [X] T050 [US3] Test sorting alphabetically by title
- [X] T051 [US3] Test combining sort with filters

## Phase 6: Integration & Validation

### Goal
Integrate all features and ensure they work together without breaking existing functionality.

### Independent Test Criteria
- All new features work together
- Basic functionality remains intact
- Performance requirements are met
- Error handling is appropriate

### Tasks
- [X] T052 Update main.py to include all new CLI commands
- [X] T053 Test integration of priority/tags with search/filter
- [X] T054 Test integration of sorting with search/filter
- [X] T055 Verify all Basic Level features still work unchanged
- [X] T056 Test performance with 100+ tasks for search/filter operations
- [X] T057 Test performance with 100+ tasks for sort operations
- [X] T058 Add error handling for invalid priority values
- [X] T059 Add error handling for invalid tag formats
- [X] T060 Add error handling for empty search results
- [X] T061 Add error handling for invalid filter combinations

## Phase 7: Polish & Cross-Cutting Concerns

### Goal
Complete the implementation with documentation, help text, and final quality checks.

### Independent Test Criteria
- CLI provides helpful error messages
- Help text is clear and comprehensive
- All functionality is properly documented

### Tasks
- [ ] T062 Update CLI help text for all new commands and options
- [ ] T063 Add examples to CLI help for new functionality
- [ ] T064 Update README.md with documentation for new features
- [ ] T065 Create comprehensive test suite covering all features
- [ ] T066 Run all tests to ensure everything works together
- [ ] T067 Verify no breaking changes to Basic Level functionality
- [ ] T068 Document new CLI commands in README.md
- [ ] T069 Final validation that all acceptance criteria from spec are met

## Dependencies

User Story 1 (P1) must be completed before User Stories 2 and 3, as search and filter functionality requires tasks to have priority and tag fields.

User Stories 2 and 3 (P1 and P2) can be developed in parallel once User Story 1 is complete.

## Parallel Execution Examples

**User Story 1 parallel tasks:**
- T016-T017 (create_task updates) can run in parallel with T018-T019 (update_task updates)
- T020-T021 (CLI add flags) can run in parallel with T022-T023 (CLI update commands)

**User Story 2 parallel tasks:**
- T028 (search) can run in parallel with T029-T031 (filter functions)
- T033 (search command) can run in parallel with T034-T036 (filter options)

**User Story 3 parallel tasks:**
- T044 (priority sort) can run in parallel with T045 (alphabetical sort)

## Implementation Strategy

1. **MVP First**: Complete User Story 1 (Priority & Tags) as the minimum viable product
2. **Incremental Delivery**: Add search/filter functionality next
3. **Complete Feature Set**: Add sorting functionality last
4. **Integration**: Ensure all features work together seamlessly
5. **Polish**: Complete documentation and final validation