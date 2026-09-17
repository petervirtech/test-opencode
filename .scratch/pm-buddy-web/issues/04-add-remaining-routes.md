# 04: Add remaining routes (`/epic/<id>`, `/add_feature/<int:epic_id>`, `/feature/<int:fid>`, `/add_story/<int:fid>`)

**What to build:** Full CRUD navigation for epics, features and stories.

**Blocked by:** 02 & 03 (templates required)

**Status:** done
- [x] `/epic/<int:epic_id>` shows epic details and its features.
- [x] `/add_feature/<int:epic_id>` handles GET/POST to create a feature.
- [x] `/feature/<int:fid>` shows feature details and its stories.
- [x] `/add_story/<int:fid>` handles GET/POST to create a story.

## Comments

- 2026-09-16: Implemented. Routes render `epic_detail.html`, `feature_detail.html` and `add_story.html`; verified by `src/pm_buddy/test_webapp.py`.
