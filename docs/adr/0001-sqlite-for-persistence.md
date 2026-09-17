# SQLite for Persistence

**Context:** The PM Buddy application is intended to run as a lightweight, Windows‑only tool for individual project managers. It needs a simple, zero‑configuration data store that works out of the box with Python.

**Decision:** Use SQLite (`pm_buddy.db`) as the default persistence layer, with an overridable path for tests.

**Why:** SQLite is bundled with Python, requires no separate server process, and provides sufficient performance for the expected workload. Switching to a more scalable database (e.g., PostgreSQL) would require schema migration, data import tooling, and a different deployment model—effort that is unnecessary for the current scope.
