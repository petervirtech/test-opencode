# 03: Create core Jinja2 templates (`index.html`, `add_epic.html`)

**What to build:** Basic HTML pages that list epics and provide a form to create an epic.

**Blocked by:** 02 (routes need templates)

**Status:** done
- [x] `templates/index.html` displays a list of epics with links to their detail pages.
- [x] `templates/add_epic.html` contains a form with fields for title and description.

## Comments

- 2026-09-16: Implemented. `index.html` links each epic to `/epic/<id>`; `add_epic.html` posts title/description.
