# 02: Add Flask web‑app skeleton (index & add_epic routes)

**What to build:** Create a minimal `pm_buddy.webapp` module with `/` and `/add_epic` routes that render Jinja2 templates.

**Blocked by:** 01 (service layer must exist)

**Status:** ready-for-agent
- [ ] Flask app initialized with `app = Flask(__name__)`.
- [ ] `/` route lists epics via service layer and renders `index.html`.
- [ ] `/add_epic` route handles GET (show form) and POST (create epic, redirect).
