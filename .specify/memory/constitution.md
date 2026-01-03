<!--
Sync Impact Report:
- Version change: 1.0.0 → 1.1.0
- Modified sections: All sections updated to match detailed constitution requirements
- Added sections: Feature progression levels, enforcement rules, mandatory project structure, evaluation criteria
- Templates requiring updates: ✅ Updated
- Follow-up TODOs: None
-->

# The Evolution of Todo - Phase I: In-Memory Python Console Application Constitution

## 1. Project Title

**The Evolution of Todo**
**Phase I: In-Memory Python Console Application**

## 2. Project Overview

This project simulates the real-world evolution of software systems — from simple scripts to intelligent systems.

In **Phase I**, participants must build a **CLI-based Todo application** that evolves beyond a basic MVP by implementing **organizational and intelligent features**.

Participants act as **Product Architects**, responsible for:
- Defining specifications
- Planning feature evolution
- Enforcing architecture
- Using AI agents instead of manual coding

## 3. Project Goal

- Teach real-world software evolution
- Enforce **spec-first development**
- Prevent shallow CRUD-only projects
- Ensure progressive complexity
- Demonstrate mastery of AI-assisted development

## 4. Development Rules (Non-Negotiable)

- ❌ Manual coding is strictly forbidden
- ✅ All development must follow **Agentic Dev Stack**
- ✅ Workflow:
  1. `/sp.specify`
  2. `/sp.plan`
  3. `/sp.tasks`
  4. Code generation via **Claude Code**
- ✅ **Spec-Kit Plus** is the single source of truth
- ❌ No feature may exist without a spec
- ❌ No skipping of feature levels

## 5. Target Audience

- Hackathon participants
- Students learning AI-assisted engineering
- Future product architects

## 6. Technology Stack

- Python **3.13+**
- UV package manager
- CLI-based interface
- In-memory storage only
- Tools:
  - Spec-Kit Plus
  - Claude Code

## 7. Todo App Feature Progression (STRICT)

⚠️ **IMPORTANT RULE**

👉 **ALL feature levels must be completed in sequence: Basic → Intermediate → Advanced**

### 7.1 Basic Level (MVP) — ALL MANDATORY

These are the minimum viable features.
**Every Basic feature below must be implemented.**

- **Add Task** – Create new todo items with descriptions
- **View Task List** – Display all tasks in a readable format
- **Update Task** – Modify existing task descriptions
- **Delete Task** – Remove tasks from the list
- **Mark as Complete** – Toggle task completion status

### 7.2 Intermediate Level (Organization & Usability) — ALL MANDATORY

These features make the app usable and production-like.
**Every Intermediate feature below must be implemented.**

- **Priorities & Tags / Categories**
  - Assign priority levels: high / medium / low
  - Add multiple labels such as `work`, `home`, `personal`

- **Search & Filter**
  - Search tasks by keyword
  - Filter by:
    - Completion status
    - Priority
    - Date (if available)

- **Sort Tasks**
  - Sort tasks by:
    - Priority
    - Alphabetical order
    - Due date

### 7.3 Advanced Level (Intelligent Features) — ALL MANDATORY

These features introduce automation and intelligence.
**Every Advanced feature below must be implemented.**

- **Recurring Tasks**
  - Automatically reschedule repeating tasks
  - Support patterns like:
    - Daily
    - Weekly
    - Custom intervals

- **Due Dates & Time Reminders**
  - Assign due dates with date & time
  - Trigger reminders (CLI or environment-based)
  - Handle overdue tasks gracefully

## 8. Enforcement Rule (Critical)

🚫 A project will be considered **INVALID** if:

- Any Intermediate feature is missing
- Any Advanced feature is missing
- Features exist without specs
- Manual code is written
- Only Basic CRUD is implemented

There are **NO OPTIONAL FEATURES** in Phase I.

## 9. Functional Requirements

Phase I must include:

- All Basic features
- All Intermediate features
- All Advanced features
- CLI commands for every feature
- Clear user feedback for each operation

## 10. Non-Functional Requirements

- Clean architecture
- Separation of concerns:
  - Models
  - Services
  - CLI layer
- Readable AI-generated Python code
- Consistent command structure
- Error handling for invalid inputs

## 11. Data Constraints

- In-memory data only
- No file persistence
- No databases
- Data resets on program exit

## 12. Mandatory Project Structure

```
/
├── Constitution.md
├── specs/
│   ├── spec-1.md
│   ├── spec-2.md
│   ├── spec-3.md
│   └── ...
├── src/
│   └── todo/
│       ├── __init__.py
│       ├── main.py        # CLI entry point
│       ├── models.py     # Data models
│       ├── services.py   # Business logic
│       └── cli.py        # CLI interaction layer
├── README.md
├── CLAUDE.md
└── pyproject.toml
```

## 13. Documentation Requirements

- Constitution.md – Rules & enforcement
- specs/ – Full history of all specs (Basic → Advanced)
- README.md – Setup & CLI usage
- CLAUDE.md – AI behavior & constraints

## 14. Evaluation Criteria

Judging will be based on:
- Completion of ALL feature levels
- Spec clarity and traceability
- Proper Agentic Dev Stack usage
- Architectural cleanliness
- Functional CLI behavior
- AI-driven development discipline

## 15. Definition of Done (Phase I)

Phase I is considered DONE only if:
- All Basic features work
- All Intermediate features work
- All Advanced features work
- Specs exist for every feature
- Claude Code generated all code
- Repository follows required structure

## 16. Final Statement

This constitution enforces progressive complexity.
A Todo app that stops at CRUD is not acceptable.
Only projects that fully evolve through:
 Basic → Intermediate → Advanced
 will be accepted.

## Governance

Constitution supersedes all other practices; Amendments require documentation and approval; All development must follow the Agentic Dev Stack workflow; Manual code writing is strictly prohibited

**Version**: 1.1.0 | **Ratified**: 2025-12-31 | **Last Amended**: 2026-01-02