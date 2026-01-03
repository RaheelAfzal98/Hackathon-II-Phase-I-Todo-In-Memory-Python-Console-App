---
id: 3
title: intermediate-features-plan
stage: plan
date: 2026-01-02
surface: agent
model: haiku-4-5-20251001
feature: intermediate-features
branch: 001-intermediate-features
user: Hp
command: sp.plan
labels: ["intermediate-features", "todo-app", "plan", "architecture", "cli"]
links:
  spec: specs/001-intermediate-features/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-intermediate-features/plan.md
  - specs/001-intermediate-features/research.md
  - specs/001-intermediate-features/data-model.md
  - specs/001-intermediate-features/quickstart.md
  - specs/001-intermediate-features/contracts/todo-service-contract.md
tests:
  - none
---

## Prompt

```text
Intermediate Level Implementation Plan – Phase I CLI Todo App

Project Context:
This plan follows the approved `/sp.specify` for Intermediate Level features of
"The Evolution of Todo – Phase I".
Basic Level features are already implemented and must not be modified.

Objective:
Create a clear, step-by-step implementation plan for adding Intermediate Level
organizational and usability features to the existing in-memory CLI Todo
application using Claude Code and Spec-Kit Plus.

Scope:
This plan applies ONLY to Intermediate Level features:
- Priorities & Tags / Categories
- Search & Filter
- Sort Tasks

No Advanced Level features are allowed in this plan.

Planning Principles:
- No manual coding
- All code generated via Claude Code
- Every step must map directly to the approved specification
- Maintain clean architecture and separation of concerns
- Avoid refactoring Basic Level behavior unless strictly required for extension

---

Plan Breakdown:

Step 1: Model Extensions
- Extend the existing Todo data model to support:
  - Priority field (enum-like: high, medium, low)
  - Tags/categories (list of strings)
- Ensure default values do not break existing tasks
- Maintain backward compatibility with Basic Level features

Step 2: Service Layer Enhancements
- Update service logic to:
  - Create tasks with optional priority and tags
  - Update priority and tags for existing tasks
- Implement search functionality:
  - Keyword matching on title and description
- Implement filtering logic:
  - By completion status
  - By priority
  - By tag/category
- Implement sorting logic:
  - By priority (high → low)
  - Alphabetically by title
- Ensure sorting operations do not mutate stored task data

Step 3: CLI Command Design
- Define new CLI commands or flags for:
  - Setting priority and tags during task creation
  - Updating priority and tags
  - Searching tasks by keyword
  - Filtering tasks by status, priority, or tag
  - Sorting task lists during view operations
- Ensure CLI commands are consistent with existing Basic Level commands
- Provide clear CLI output and user feedback

Step 4: Integration & Flow Validation
- Integrate Intermediate features with existing Basic Level flows
- Verify that:
  - Add, Update, Delete, View, Mark Complete still work as before
  - New features do not introduce breaking changes
- Handle edge cases:
  - Invalid priority values
  - Empty search results
  - Non-existent tags or filters

Step 5: Documentation Updates
- Update README.md:
  - Document new CLI commands for Intermediate features
- Ensure specs folder contains:
  - The Intermediate Level specification file
- Confirm CLAUDE.md continues to enforce:
  - No manual coding
  - Spec-first development

---

Deliverables:
- Updated Todo model supporting priority and tags
- Enhanced service layer for search, filter, and sort
- Extended CLI supporting all Intermediate commands
- No changes to Basic Level feature behavior
- All changes traceable back to the Intermediate specification

Success Criteria:
- All Intermediate Level features function correctly via CLI
- Basic Level features remain unchanged and stable
- Code
```

## Response snapshot

```text
# Implementation Plan: Intermediate Level Features for Phase I CLI Todo App

**Branch**: `001-intermediate-features` | **Date**: 2026-01-02 | **Spec**: [specs/001-intermediate-features/spec.md](specs/001-intermediate-features/spec.md)
**Input**: Feature specification from `/specs/001-intermediate-features/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implementation of Intermediate Level features for the CLI Todo application, including Priority and Tag support for tasks, Search and Filter functionality, and Task Sorting capabilities. These features enhance the basic todo functionality with organizational and usability improvements while maintaining in-memory storage and CLI-based interface. The implementation will extend the existing Todo model, enhance service layer functionality, and add new CLI commands while preserving all Basic Level features.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: Standard library only (no external dependencies for core functionality)
**Storage**: In-memory only (N/A - no persistent storage)
**Testing**: pytest for unit and integration tests
**Target Platform**: Cross-platform CLI application (Windows, macOS, Linux)
**Project Type**: Single project CLI application
**Performance Goals**: <10 seconds for search/filter operations regardless of task count, <5 seconds for sorting operations
**Constraints**: <200MB memory usage, maintain backward compatibility with Basic Level features, in-memory data only
**Scale/Scope**: Support for up to 10,000 tasks in memory

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- ✅ **Spec-First Development**: Following approved spec from `/sp.specify`
- ✅ **AI-Assisted Coding**: All code will be generated via Claude Code
- ✅ **Spec-Driven Development**: Implementation based on approved specification
- ✅ **Clean Architecture**: Will maintain separation of concerns (models, services, CLI)
- ✅ **In-Memory Constraint**: Will maintain in-memory only storage as required
- ✅ **Functional Completeness**: Will implement all specified Intermediate features
- ✅ **Technology Stack Requirements**: Using Python 3.13+ as required
- ✅ **Development Workflow**: Following Agentic Dev Stack (specify → plan → tasks → implement)
- ✅ **Governance**: Following constitution requirements for amendments and approval

## Project Structure

### Documentation (this feature)

```text
specs/001-intermediate-features/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
src/
├── todo/
│   ├── __init__.py
│   ├── main.py          # CLI entry point
│   ├── models.py        # Data models (TodoItem with priority/tags)
│   ├── services.py      # Business logic (search, filter, sort)
│   └── cli.py           # CLI interaction layer
├── tests/
│   ├── unit/
│   ├── integration/
│   └── contract/
├── pyproject.toml
├── README.md
└── CLAUDE.md
```

**Structure Decision**: Single project CLI application structure selected, following the mandatory project structure defined in the constitution. The application will maintain the clean architecture with clear separation of concerns between models, services, and CLI layers.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [N/A] | [No violations identified] | [All constitution requirements met] |
```

## Outcome

- ✅ Impact: Created comprehensive implementation plan for intermediate features (priorities, tags, search, filter, sort) with research, data model, quickstart guide, and contracts
- 🧪 Tests: none
- 📁 Files: specs/001-intermediate-features/plan.md, specs/001-intermediate-features/research.md, specs/001-intermediate-features/data-model.md, specs/001-intermediate-features/quickstart.md, specs/001-intermediate-features/contracts/todo-service-contract.md
- 🔁 Next prompts: Ready for /sp.tasks to create implementation tasks
- 🧠 Reflection: The plan successfully addresses all required Intermediate Level features while maintaining backward compatibility with Basic Level features. The architecture maintains clean separation of concerns between models, services, and CLI layers as required by the constitution.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Create implementation tasks using /sp.tasks