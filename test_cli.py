#!/usr/bin/env python3
"""Test script to verify the command-line interface functionality."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from todo.main import run_command_line_interface

def test_cli_add():
    """Test adding a task via CLI."""
    print("Testing CLI Add Task...")
    sys.argv = ['test', 'add', 'Test CLI Task', 'Testing command line interface']
    try:
        run_command_line_interface()
    except SystemExit:
        pass  # Expected after successful command execution

def test_cli_list():
    """Test listing tasks via CLI."""
    print("\nTesting CLI List Tasks...")
    sys.argv = ['test', 'list']
    try:
        run_command_line_interface()
    except SystemExit:
        pass  # Expected after successful command execution

def test_cli_complete():
    """Test completing a task via CLI (will fail since we don't know the ID)."""
    print("\nTesting CLI Complete Task (with mock ID)...")
    # First we'd need to get an actual task ID, so this will fail as expected
    sys.argv = ['test', 'complete', 'nonexistent-id']
    try:
        run_command_line_interface()
    except SystemExit:
        pass  # Expected after command execution

if __name__ == "__main__":
    test_cli_add()
    test_cli_list()
    test_cli_complete()