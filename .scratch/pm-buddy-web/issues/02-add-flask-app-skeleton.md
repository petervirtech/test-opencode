# 02: Add Flask web‑app skeleton (index & add_epic routes)

**What to build:** Create a minimal `pm_buddy.webapp` module with `/` and `/add_epic` routes that render Jinja2 templates.

**Blocked by:** 01 (service layer must exist)

**Status:** done
- [x] Flask app initialized with `app = Flask(__name__)`.
- [x] `/` route lists epics via service layer and renders `index.html`.
- [x] `/add_epic` route handles GET (show form) and POST (create epic, redirect).

## Comments

- 2026-09-16: Implemented. Verified by `src/pm_buddy/test_webapp.py` via the Flask test client.
