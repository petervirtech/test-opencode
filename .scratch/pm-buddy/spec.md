# PM Buddy Spec

## Problem Statement
The user needs a lightweight product‑manager companion that runs on Windows desktops where only Python is available. The tool should allow a PM to manage Epics, Features and User Stories locally in an SQLite database, with the ability to sync a hybrid Azure DevOps (TFS) integration later.

## Solution
A console‑based Python application that:
* Stores a mid‑level backlog model (Epic → Feature → Story) in SQLite.
* Provides CRUD operations for Epics, Features and Stories via a simple menu.
* Exposes a stub Azure DevOps adapter for future sync.

The design keeps the UI minimal, uses only standard library modules and SQLite (bundled with Python), so it runs on any Windows machine without additional installs.

## User Stories
1. As a PM, I want to list all Epics so that I can see the high‑level backlog.
2. As a PM, I want to add an Epic so that I can start defining work.
3. As a PM, I want to list all Features of an Epic so that I can drill down.
4. As a PM, I want to add a Feature under an Epic so that I can organise work.
5. As a PM, I want to list all Stories of a Feature so that I can track detail.
6. As a PM, I want to add a Story under a Feature so that I can capture requirements.
7. As a PM, I want to set the status of an Epic/Feature/Story so that I can track progress.
8. As a PM, I want the tool to persist data locally so that my backlog survives restarts.
9. As a PM, I want the tool to use SQLite so that it runs on Windows without external DB servers.
10. As a PM, I want a stub Azure DevOps adapter so that future sync logic can be added.
11. As a PM, I want unit tests for the database layer so that changes are safe.
12. As a PM, I want to run tests with `python -m unittest` so that CI can be added.
13. As a PM, I want the code to follow PEP‑8 and type hints so that it is maintainable.
14. As a PM, I want the code to be packaged as `pm_buddy` so that it can be imported.
15. As a PM, I want the UI to exit cleanly so that it can be used in scripts.

## Implementation Decisions
- **Modules**: `pm_buddy.app` contains the data model, SQLite helper (`DB`) and console UI. The Azure adapter is a separate class in the same module.
- **Seam**: The highest seam is the `DB` class; all persistence logic is isolated here. UI and Azure adapter depend only on this interface.
- **Data Model**: Mid‑level model with dataclasses `Epic`, `Feature`, `Story`. Relationships are represented by foreign keys in SQLite.
- **SQLite Schema**: Three tables (`epics`, `features`, `stories`) with primary keys and foreign key constraints. Status is a simple text field.
- **Testing**: Tests exercise `DB` using an in‑memory SQLite database. No UI tests are required.
- **Azure Adapter**: Stub methods `sync_to_azure` and `sync_from_azure`; no external calls.
- **Packaging**: The package is a simple namespace; `__init__.py` marks the directory.
- **Entry Point**: The script can be run directly; `main()` contains the menu loop.

## Testing Decisions
- Tests focus on external behavior: adding an Epic and retrieving it, verifying IDs and fields.
- `DB` is the only module under test; UI logic is trivial and not unit‑tested.
- The test uses an in‑memory SQLite database to avoid side effects.

## Out of Scope
- Full Azure DevOps integration and authentication.
- A graphical UI or web interface.
- Advanced status transitions (e.g., gating, dependencies).

## Further Notes
The current implementation is intentionally minimal to satisfy the “run on Windows with only Python” constraint. Future work can add a richer UI, persistence options and Azure sync.
