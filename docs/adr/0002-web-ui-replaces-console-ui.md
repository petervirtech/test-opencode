# Web UI Replaces the Console UI

**Context:** PM Buddy originally shipped with a console menu as its interface, later joined by a Flask web UI. The two interfaces duplicated the same create/browse operations with no shared layout or identity, and the console UI served no purpose the web UI did not already cover.

**Decision:** The web UI is the sole interface. The console entry point and its menu loop are deleted, and the former grab‑bag `app` module is split into single‑purpose modules: `models` (Status, Epic, Feature, Story), `database` (the DB class), and `adapter` (the Azure DevOps stub). The web app is started with `PYTHONPATH=src python -m pm_buddy.webapp`.

**Why:** One interface means one place to maintain, style, and extend. The web UI is a superset of the console UI's capabilities (create + browse), so removing the console loses no functionality. A single interface also makes the CBS‑branded layout the only visual language users ever see.
