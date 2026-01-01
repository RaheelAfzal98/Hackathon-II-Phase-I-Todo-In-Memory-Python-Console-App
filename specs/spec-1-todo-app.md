# Spec-1: In-Memory CLI Todo Application (Phase I)

---

## Spec Title

**In-Memory Command-Line Todo Application**

---

## Problem Statement

Students need a simple but well-structured Todo application that demonstrates the **foundational stage of software evolution**. The system must work entirely in memory, be operated through the command line, and be developed using **spec-driven, AI-assisted development** without manual coding.

This specification defines the **minimum viable functionality and architecture** required for Phase I of *The Evolution of Todo* project.

---

## Target Users

- Students participating in the hackathon
- Learners acting as Product Architects
- Developers practicing spec-driven and AI-assisted development

---

## Scope of This Specification

This spec covers:
- A single-user
- In-memory
- Command-line Todo application

This spec does **not** include:
- Persistent storage
- Web or GUI interfaces
- Multi-user support
- Advanced or AI-powered features

---

## Functional Requirements

### FR-1: Add Todo Task

**Description:**
The system must allow the user to add a new todo task.

**Acceptance Criteria:**
- User can provide:
  - Title (required)
  - Description (optional)
- System assigns a unique ID to each task
- Newly added task is marked as **Incomplete** by default

---

### FR-2: View All Tasks

**Description:**
The system must display all existing todo tasks.

**Acceptance Criteria:**
- Tasks are listed in a readable CLI format
- Each task displays:
  - ID
  - Title
  - Description
  - Completion status (Complete / Incomplete)
- If no tasks exist, a clear message is shown

---

### FR-3: Update Todo Task

**Description:**
The system must allow modification of an existing task.

**Acceptance Criteria:**
- User specifies task by ID
- User can update:
  - Title
  - Description
- System confirms successful update
- If ID does not exist, an error message is shown

---

### FR-4: Delete Todo Task

**Description:**
The system must allow deletion of a task.

**Acceptance Criteria:**
- User deletes a task using its ID
- Task is permanently removed from memory
- Confirmation message is shown
- Invalid IDs are handled gracefully

---

### FR-5: Mark Task as Complete / Incomplete

**Description:**
The system must allow toggling task completion status.

**Acceptance Criteria:**
- User specifies task by ID
- Task status toggles between:
  - Complete
  - Incomplete
- Updated status is reflected when viewing tasks

---

## Non-Functional Requirements

### NFR-1: In-Memory Data Handling
- All tasks must be stored in memory only
- Data must reset when the application exits

### NFR-2: CLI Usability
- Commands must be simple and intuitive
- Clear prompts and feedback messages must be shown

### NFR-3: Code Quality
- Code must be clean, modular, and readable
- Proper separation of concerns:
  - Models
  - Services
  - CLI layer

### NFR-4: Error Handling
- Invalid inputs must not crash the application
- User-friendly error messages must be displayed

---

## Data Model (Logical)

### Todo Task
- `id`: unique identifier (integer)
- `title`: short text
- `description`: longer text
- `is_completed`: boolean

---

## CLI Interaction Flow (High-Level)

1. Start application
2. Display menu options:
   - Add task
   - View tasks
   - Update task
   - Delete task
   - Mark complete/incomplete
   - Exit
3. User selects an option
4. System performs action and shows result
5. Loop until user exits

---

## Constraints & Rules

- Manual coding is not allowed
- All code must be generated via **Claude Code**
- Spec-Kit Plus governs all changes and iterations
- This spec must be versioned and preserved in `/specs`

---