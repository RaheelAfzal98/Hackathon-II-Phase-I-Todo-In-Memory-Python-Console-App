# Quickstart Guide: Advanced Todo Features

## Overview
This guide provides a quick overview of how to implement the Advanced Todo Features including recurring tasks and due dates & time reminders.

## Implementation Steps

### 1. Update Data Model (models.py)
- Extend the Todo dataclass with new fields:
  - `due_date: Optional[datetime]`
  - `is_recurring: bool`
  - `recurrence_pattern: Optional[str]`
  - `recurrence_interval: Optional[int]`
- Update TodoModel to handle these new fields in all operations
- Add logic for generating next occurrence of recurring tasks

### 2. Update Service Layer (services.py)
- Add methods to handle due date and recurrence logic
- Implement overdue task detection
- Add recurrence pattern validation
- Update existing methods to work with new fields
- Add logic to generate new occurrences when recurring tasks are completed

### 3. Update CLI Interface (cli.py)
- Add options to create tasks with due dates and recurrence patterns
- Update display methods to show due dates and recurrence information
- Add overdue status indicators
- Add menu options for advanced features

### 4. Update Main Application (main.py)
- Add command-line arguments for due dates and recurrence
- Update argument parsing to handle new options
- Ensure all new functionality is accessible via CLI

## Key Implementation Points

### Recurring Task Logic
- When a recurring task is completed, create a new occurrence with updated due date
- Respect recurrence patterns: daily (next day), weekly (next week), custom (based on interval)
- Maintain original task properties in new occurrences

### Due Date Handling
- Store due dates as datetime objects
- Compare against current time to determine overdue status
- Display clear indicators for overdue tasks

### CLI Integration
- Maintain backward compatibility with existing commands
- Add new optional parameters without breaking existing functionality
- Provide clear feedback for all operations

## Testing Approach
- Unit test all new methods in isolation
- Integration test the complete workflow for recurring tasks
- Verify that existing functionality remains unchanged
- Test edge cases like invalid recurrence patterns and past due dates

## Architecture Notes
- Keep the separation of concerns: models handle data, services handle logic, CLI handles interface
- No external dependencies should be introduced
- All data remains in-memory as per constraints
- Time-based operations happen during CLI execution only, no background processes