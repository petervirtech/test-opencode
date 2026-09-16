# 04: Add remaining routes (`/epic/<id>`, `/add_feature/<int:epic_id>`, `/feature/<int:fid>`, `/add_story/<int:fid>`)

**What to build:** Full CRUD navigation for epics, features and stories.

**Blocked by:** 02 & 03 (templates required)

**Status:** ready-for-agent
- [ ] `/epic/<int:epic_id>` shows epic details and its features.
- [ ] `/add_feature/<int:epic_id>` handles GET/POST to create a feature.
- [ ] `/feature/<int:fid>` shows feature details and its stories.
- [ ] `/add_story/<int:fid>` handles GET/POST to create a story.
