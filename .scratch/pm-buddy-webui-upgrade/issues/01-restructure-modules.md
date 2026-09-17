# 01: Split the app module; remove the console UI

**What to build:** PM Buddy becomes a web-only product with a clean module structure. The grab-bag app module is split into three single-purpose modules — domain model (Status, Epic, Feature, Story), database access, and the Azure adapter stub — and the console entry point is deleted. The service and web app modules import from the new homes, the sync route keeps working, and the documentation (README plus a new ADR) records that the web UI is now the sole interface. From the user's perspective: there is exactly one way to run the tool, and the docs say so.

**Blocked by:** None (can start immediately)

**Status:** done

- [x] The domain model (Status enum, Epic/Feature/Story dataclasses) lives in a dedicated model module
- [x] Database access (the DB class) lives in a dedicated database module
- [x] The Azure adapter stub lives in a dedicated adapter module
- [x] The old grab-bag app module, including its console entry point, is deleted
- [x] The service module and the web app module import from the new modules; the sync route still works
- [x] The existing database tests move to a test file matching the new module name, unchanged in content, and pass
- [x] The full test suite passes
- [x] The README describes the web-only product: Flask as a prerequisite, the correct run command, and no Windows-desktop / console-menu / no-external-packages claims
- [x] ADR 0002 records that the web UI replaces the console UI as the sole interface
