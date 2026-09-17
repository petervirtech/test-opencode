# 06: Unit‑test `PMBuddyService` CRUD logic

**What to build:** Tests that verify adding/listing epics, features and stories using an in‑memory SQLite DB.

**Blocked by:** 01 (service layer must exist)

**Status:** done
- [x] Test adding an epic and retrieving it.
- [x] Test adding a feature under the created epic and listing features.
- [x] Test adding a story under the created feature and listing stories.
- [x] Verify that IDs are correctly assigned and persisted.

## Comments

- 2026-09-16: Implemented as `src/pm_buddy/test_service.py` (4 tests). Uses a temp-file DB rather than `:memory:` because the service opens a new connection per operation and each `:memory:` connection is private; the temp file gives the same isolation without side effects.
