# PM Buddy Domain

The domain of the PM Buddy application models work items in a hierarchical structure: Epics contain Features, and Features contain Stories. Each item has a title, optional description, and a status that tracks its progress.

## Language

**Epic**:
A high‑level body of work that represents a significant feature or capability. Epics are broken down into smaller Features.
_Avoid_: Initiative, Capability

**Feature**:
A concrete piece of functionality that delivers value to a user. Features belong to an Epic and may contain multiple Stories.
_Avoid_: Requirement, User Story

**Story**:
A small unit of work that can be completed in a single iteration. Stories belong to a Feature.
_Avoid_: Task, Ticket

**Status**:
The current state of an item. Possible values are *To Do*, *In Progress*, and *Done*.
_Avoid_: State, Phase
