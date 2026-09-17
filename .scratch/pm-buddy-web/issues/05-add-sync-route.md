# 05: Add “Sync to Azure DevOps” route (stub)

**What to build:** `/sync` endpoint that calls `AzureAdapter.sync_to_azure()` and redirects.

**Blocked by:** 02 (Flask app exists)

**Status:** done
- [x] `/sync` route defined.
- [x] Calls stub `AzureAdapter.sync_to_azure()`.
- [x] Redirects to home page after execution.

## Comments

- 2026-09-16: Implemented. Fixed a latent bug: the route referenced a non-existent `service.db`; it now builds `DB(db_path=service.db_path)`. Verified by `test_sync_redirects_to_index`.
