# 07: Flask integration tests (test client)

**What to build:** Tests that GET `/`, POST `/add_epic` and other endpoints return 200, redirect correctly, and render expected content.

**Blocked by:** 04 & 03 (templates + routes ready)

**Status:** done
- [x] GET `/` returns 200 and lists existing epics.
- [x] POST to `/add_epic` creates an epic, redirects to home, and the new epic appears.
- [x] GET `/epic/<id>` shows features for that epic.
- [x] POST to `/add_feature/<epic_id>` creates a feature and redirects appropriately.
- [x] GET `/feature/<id>` shows stories for that feature.
- [x] POST to `/add_story/<fid>` creates a story and redirects appropriately.

## Comments

- 2026-09-16: Implemented in `src/pm_buddy/test_webapp.py` (8 tests via the Flask test client, temp-file DB). Also covers the `/sync` redirect.
