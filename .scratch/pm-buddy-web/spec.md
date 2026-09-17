# PM Buddy Web UI Spec

## Problem Statement
Users of PM Buddy need a quick, browser‑based way to create new Epics in the backlog. The existing console UI is functional but inconvenient for everyday use, and no web interface currently exists to add Epics.

## Solution
Introduce a lightweight Flask + Jinja2 web application that:
- Renders an “Add Epic” form.
- Persists the new Epic to the same SQLite database used by the console UI.
- Redirects back to the list of Epics upon successful creation.

This satisfies the user’s need for a convenient, Windows‑only web interface while keeping all persistence logic in the existing `PMBuddyService`.

## User Stories
1. As a PM, I want to view the “Add Epic” page so that I can start planning.
2. As a PM, I want to enter an Epic title and optional description so that the backlog reflects my intent.
3. As a PM, I want to submit the form and be redirected to the Epic list so that I can verify creation.
4. As a developer, I want the form submission to be processed by Flask’s test client so that route logic can be unit‑tested.
5. As a developer, I want the service layer to handle database access so that UI code remains thin.
6. As a developer, I want the `PMBuddyService` to open a new SQLite connection per request so that thread‑safety is preserved.
7. As a PM, I want the Epic list page to display all Epics so that I can see high‑level work.
8. As a PM, I want the “Add Epic” link on the list page so that navigation is intuitive.
9. As a developer, I want templates to be simple Jinja2 files so that they are easy to maintain.
10. As a developer, I want the web app to run on Windows with only Python installed so that no additional setup is required.
11. As a developer, I want the service layer to expose `add_epic`, `list_epics` so that tests can call them directly.
12. As a developer, I want the web routes to delegate all business logic to `PMBuddyService` so that responsibilities are clear.
13. As a developer, I want the Flask app to be testable with `app.test_client()` so that HTTP behavior can be verified.
14. As a developer, I want the database path to default to `pm_buddy.db` but be overridable for tests so that test isolation is possible.
15. As a developer, I want the web app to use the existing `pm_buddy/templates/` directory so that all UI code stays in one place.

## Implementation Decisions
- **Modules Modified**: `pm_buddy/webapp.py`, `pm_buddy/service.py`, and the new template `add_epic.html`.
- **Seam**: The highest seam is `PMBuddyService`; all Flask routes delegate to it.
- **Database Access**: `PMBuddyService` now opens a fresh SQLite connection per operation (`DB(db_path=self.db_path)`) to avoid thread‑safety issues.
- **Template Location**: Templates live in `pm_buddy/templates/`; Flask’s `template_folder` is set to that directory.
- **Form Handling**: POST to `/add_epic` creates an Epic via `service.add_epic(title, description)` and redirects to `/`.
- **Error Handling**: Validation is minimal; missing title results in a 400 response (not implemented yet but noted for future work).
- **Thread Safety**: Each request obtains a new `DB` instance; no shared connection is kept in the service.
- **Testing**: The test client uses `app.test_client()`; tests exercise GET and POST routes without touching the database directly.

## Testing Decisions
- **External Behavior Focus**: Tests assert HTTP status codes, redirects, and content of rendered pages. They do not inspect the internal state of `DB` or `PMBuddyService`.
- **Modules Tested**:  
  * `pm_buddy.webapp` – route handling, rendering.  
  * `pm_buddy.service` – CRUD operations via fresh DB connections.
- **Prior Art**: Existing `pm_buddy/test_app.py` tests database CRUD; new web tests mirror that pattern but use Flask’s test client.
- **Isolation**: Tests use a temp‑file SQLite database to avoid side effects. (A plain `:memory:` DB cannot be used because the service opens a new connection per operation and each `:memory:` connection is private.)

## Out of Scope
- Full validation and error pages for malformed input.
- Authentication or authorization layers.
- Advanced status transitions beyond “To Do”.
- Integration with Azure DevOps (the stub remains unchanged).
- Styling or JavaScript enhancements.

## Further Notes
- The real Flask package is required for both unit tests and manual execution. (An earlier local `src/flask` stub was removed: it was syntactically broken and could never be imported.)
- Future iterations may add a `sync` route to push changes to Azure DevOps, but that is outside the current scope.
