# Research: Advanced Todo Features Implementation

## Objective
Research and document technical approaches for implementing recurring tasks and due dates with time reminders in the CLI Todo application, while maintaining in-memory storage and CLI-only constraints.

## Research Areas

### 1. Recurring Task Implementation Patterns

**Decision**: Implement recurrence using interval-based scheduling with datetime calculations
**Rationale**: Simple and effective approach that works within in-memory constraints without external dependencies
**Alternatives considered**:
- CRON expressions: Too complex for this use case and would require external libraries
- Pre-scheduled tasks: Would require background processes which are not allowed
- Interval-based scheduling: Clean, simple, and fits the requirements perfectly

### 2. Due Date and Time Storage

**Decision**: Use Python's datetime module to store and compare due dates
**Rationale**: Built-in Python functionality that handles timezone and comparison operations effectively
**Alternatives considered**:
- Unix timestamps: Less readable and harder to debug
- String representations: Would require custom parsing and comparison logic
- datetime objects: Native Python support with rich comparison methods

### 3. Time Reminder Mechanism

**Decision**: Implement time reminders as status checks during CLI operations (non-blocking)
**Rationale**: Safe for CLI execution, no background processes required, and provides timely notifications
**Alternatives considered**:
- Background threads: Prohibited by requirements and could cause issues with CLI
- External scheduling: Violates the no-external-dependencies constraint
- Status checks during operations: Safe, simple, and effective for CLI context

### 4. Recurrence Pattern Types

**Decision**: Implement three recurrence patterns (daily, weekly, custom interval) as specified
**Rationale**: Directly matches the specification requirements and provides good user flexibility
**Implementation**:
- Daily: Every 1 day
- Weekly: Every 7 days
- Custom: User-defined interval in days

### 5. Task State Management for Recurring Tasks

**Decision**: Mark original task as complete and create new occurrence with updated due date
**Rationale**: Maintains task history while creating fresh instances for new periods
**Alternatives considered**:
- Reset the same task: Would lose completion history
- Mark as "completed" but keep active: Would confuse users about task status
- Create new task instance: Maintains history and provides fresh task for new period

### 6. Overdue Task Detection

**Decision**: Check for overdue status during display operations by comparing due date to current time
**Rationale**: Efficient approach that only evaluates when needed for display
**Implementation**: Simple datetime comparison during list/search/filter operations

### 7. Data Model Extensions

**Decision**: Extend existing Todo model with recurrence and due date fields
**Rationale**: Maintains backward compatibility while adding required functionality
**Fields to add**:
- `due_date`: Optional datetime for due date
- `recurrence_pattern`: Optional pattern (daily, weekly, custom)
- `recurrence_interval`: Optional interval in days for custom patterns
- `is_recurring`: Boolean flag to identify recurring tasks

## Technical Constraints Resolved

1. **No external dependencies**: Using only Python standard library (datetime, dataclasses)
2. **In-memory only**: All data structures remain in application memory
3. **No background processes**: Time checks happen during CLI operations only
4. **CLI safety**: All operations are synchronous and non-blocking
5. **Backward compatibility**: Existing functionality remains unchanged