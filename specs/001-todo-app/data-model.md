# Data Model: In-Memory CLI Todo Application

## Entity: Todo Task

**Description**: Represents a single todo item in the application

**Fields**:
- `id`: string (UUID4 format) - unique identifier for the task
- `title`: string - short text describing the task
- `description`: string - longer text providing details about the task
- `completed`: boolean - indicates whether the task is completed (default: false)

**Validation Rules**:
- `id`: Must be a valid UUID4 string (auto-generated)
- `title`: Required, cannot be empty
- `description`: Optional, can be empty
- `completed`: Boolean value only (true/false)

**State Transitions**:
- New task: `completed = false` (default)
- Toggle completion: `completed = !completed`

**Relationships**: None (standalone entity)

## Data Storage Model

**Structure**: Dictionary/HashMap with UUID string keys and Todo objects as values

**Operations**:
- Add: Insert new Todo with generated UUID as key
- Read: Retrieve Todo by UUID key
- Update: Modify existing Todo fields by UUID key
- Delete: Remove Todo by UUID key
- List: Return all Todo objects in the collection

**Constraints**:
- All data stored in memory only
- Data is lost when application exits
- No duplicate IDs allowed
- Thread safety not required (single-user application)