# 07: Flask integration tests (test client)

**What to build:** Tests that GET `/`, POST `/add_epic` and other endpoints return 200, redirect correctly, and render expected content.

**Blocked by:** 04 & 03 (templates + routes ready)

**Status:** ready-for-agent
- [ ] GET `/` returns 200 and lists existing epics.
- [ ] POST to `/add_epic` creates an epic, redirects to home, and the new epic appears.
- [ ] GET `/epic/<id>` shows features for that epic.
- [ ] POST to `/add_feature/<epic_id>` creates a feature and redirects appropriately.
- [ ] GET `/feature/<id>` shows stories for that feature.
- [ ] POST to `/add_story/<fid>` creates a story and redirects appropriately.
