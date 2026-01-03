# Quickstart Guide: Intermediate Level Features for Phase I CLI Todo App

**Feature**: Intermediate Level Features (Priorities & Tags, Search & Filter, Sort Tasks)
**Date**: 2026-01-02
**Branch**: 001-intermediate-features

## Overview

This guide provides instructions for implementing the Intermediate Level features of the CLI Todo application, including Priority and Tag support, Search and Filter functionality, and Task Sorting capabilities.

## Implementation Steps

### 1. Update Data Model (`src/todo/models.py`)

- Extend the existing TodoItem class to include priority and tags fields
- Add validation for priority values ("high", "medium", "low")
- Add validation for tags (list of strings)
- Ensure backward compatibility for existing tasks

### 2. Enhance Service Layer (`src/todo/services.py`)

- Update create_task function to accept optional priority and tags
- Update update_task function to allow modifying priority and tags
- Implement search_tasks function for keyword search
- Implement filter_tasks function for filtering by status, priority, and tags
- Implement sort_tasks function for sorting by priority or title
- Add functions to combine multiple filters

### 3. Extend CLI Interface (`src/todo/cli.py`)

- Add optional arguments for priority and tags to the add command
- Add CLI commands for updating priority and tags
- Implement search command with keyword argument
- Implement filter command with options for status, priority, and tags
- Implement sort option for the list command
- Add help text and examples for all new commands

### 4. Update Main Entry Point (`src/todo/main.py`)

- Import and wire up the new CLI commands
- Ensure all new functionality is accessible through the CLI

### 5. Add Tests

- Unit tests for new model validations
- Unit tests for search, filter, and sort functions
- Integration tests for CLI commands
- Test backward compatibility with existing tasks

## Key Implementation Notes

- Maintain in-memory storage only (no persistence changes)
- Preserve all Basic Level functionality
- Ensure new features don't break existing functionality
- Use case-insensitive search for better user experience
- Allow multiple filters to be combined
- Sorting should not modify the original task list
- Validate input parameters for all new functions

## Testing Commands

After implementation, verify functionality with:

```bash
# Test priority and tags
python -m todo add "Test task" --priority high --tags work,urgent

# Test search
python -m todo search "Test"

# Test filter
python -m todo list --filter-priority high
python -m todo list --filter-status incomplete
python -m todo list --filter-tag work

# Test sort
python -m todo list --sort priority
python -m todo list --sort title
```

## Error Handling

- Validate priority values are one of "high", "medium", "low"
- Validate tag format (alphanumeric and hyphens only)
- Handle empty search results gracefully
- Handle invalid filter combinations appropriately
- Provide clear error messages for invalid inputs