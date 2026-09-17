# PM Buddy Web UI Upgrade — CBS Design System Boilerplate

Status: ready-for-agent

## Problem Statement

PM Buddy's web UI is a set of bare, unstyled HTML pages: no shared layout, no navigation, no branding. Every page is a standalone document with ad-hoc "back" links and no visual identity, so the tool feels like a prototype rather than a product. The user wants a consistent, professional web UI that follows the CBS design system (style guide at designsystem.cbs.nl), with a menu bar and room for a logo (using the cbs.nl logo as the example).

In addition, the product has outgrown its dual-interface design: the console UI is obsolete and should be removed, leaving the web UI as the sole interface. The README still describes the obsolete reality (Windows desktop, console menu, no external packages) and must be brought in line.

## Solution

From the user's perspective:

- Every page shares one boilerplate layout: a white menu bar with the CBS logo (left) and navigation links (right), a centered content area, and a minimal footer — all styled with CBS design system tokens (brand indigo `#271d6c`, blue `#0058b8`, Akko/Soho typography).
- Detail pages show breadcrumbs and render Status as a colored badge, so hierarchy and state are scannable.
- The console UI is gone; the product is web-only, and the documentation says so.

## User Stories

1. As a PM, I want every page to share the same menu bar so that I always know where I am and can navigate without hunting for links.
2. As a PM, I want the logo in the menu bar to link back to the Epic list so that I can get home with one click.
3. As a PM, I want the current section highlighted in the menu bar so that I can see which page I am on.
4. As a PM, I want the menu bar to remain usable on narrow screens (wrapping) so that I can use PM Buddy on a laptop or tablet.
5. As a PM, I want the interface styled with the CBS design system (brand colors, Akko/Soho typography) so that the tool looks professional and consistent with CBS branding.
6. As a PM, I want Status shown as a colored badge (To Do gray, In Progress blue, Done green) so that I can scan item state at a glance.
7. As a PM, I want breadcrumbs on detail pages (Epics › Epic › Feature) so that I can see my place in the hierarchy and step back.
8. As a PM, I want a minimal footer so that pages feel complete.
9. As a PM, I want the web UI to be the only interface so that there is exactly one way to use the tool.
10. As a PM, I want the README to describe how to run the web app so that I or a colleague can start it without guessing.
11. As a developer, I want a single base template that all pages inherit from so that layout changes happen in one place.
12. As a developer, I want the CBS design tokens as CSS custom properties in one stylesheet so that the visual language is centralized and tweakable.
13. As a developer, I want the CBS logo as a static asset with a text wordmark fallback so that the layout degrades gracefully if the image is missing.
14. As a developer, I want the CBS fonts loaded via @font-face with a system fallback so that the app looks right online and still renders offline.
15. As a developer, I want the domain model, database access, and Azure adapter in separate single-purpose modules so that no grab-bag "app" module remains.
16. As a developer, I want the console UI code removed so that no dead interface remains in the codebase.
17. As a developer, I want an ADR recording that the web UI replaces the console UI so that future readers understand why there is no console app.
18. As a developer, I want layout assertions in the web tests so that regressions in the shared boilerplate are caught.
19. As a developer, I want the existing database tests preserved (moved with their module) so that persistence behavior stays covered after the restructure.
20. As a developer, I want the sync route to keep working after the adapter moves so that the stub integration point is preserved.
21. As a PM, I want primary actions (Add Epic / Add Feature / Add Story) styled as buttons so that what I can do next is visually obvious.
22. As a PM, I want form fields styled with the design system (control height, border radius) so that forms look consistent with the rest of the UI.
23. As a maintainer, I want the design tokens named after the CBS palette so that future restyling maps one-to-one to the style guide.
24. As a developer, I want static assets (stylesheet, logo) served by the web framework so that no extra tooling or build step is needed.

## Implementation Decisions

- **Base template**: One Jinja base template defines the HTML skeleton — head (title block, stylesheet link, @font-face), menu bar (logo + nav links with active state), content block, footer. All six existing templates inherit from it and keep only their page-specific content.
- **Menu bar**: White background, dark text (`#091d23`), logo left, links right (Epics → index, Sync → sync route). Active link in brand indigo `#271d6c` with underline. Flex-wrap on narrow screens; no JavaScript hamburger menu (zero JS overall).
- **Logo**: The real CBS logo SVG (from cdn.cbs.nl) downloaded into the package's static assets; linked to the index route; text wordmark fallback if the image is missing.
- **Stylesheet**: One hand-written CSS file implementing the CBS design tokens as custom properties: brand `#271d6c`, blue `#0058b8`, light-aqua `#00a1cd`, text `#091d23`, grays (`#878787` / `#bdbcbc` / `#e9e9e9`), spacing scale (`.25rem`–`3rem`), border-radius `.25rem`, control height `3rem`. No Bootstrap; no link to cbs.nl's production stylesheet.
- **Typography**: @font-face for Akko (text) and Soho (titles) from cdn.cbs.nl, with a Helvetica/Arial fallback stack.
- **Content area**: Centered, max-width 1100px, horizontal padding.
- **Footer**: Minimal — app name plus one-line tagline on a light-gray background.
- **Status badges**: To Do = gray, In Progress = blue `#0058b8`, Done = green `#488225`; rendered on detail pages (and in lists where it stays readable).
- **Breadcrumbs**: On Epic and Feature detail pages, replacing the ad-hoc back links.
- **Language**: UI text stays English.
- **Console removal / restructure**: The current grab-bag app module is deleted and split into three single-purpose modules: domain model (Status enum + Epic/Feature/Story dataclasses), database access (DB class), Azure adapter (stub). The service module and web app module update their imports accordingly. The console entry point is deleted with the file.
- **Sync route**: Kept; imports the adapter from its new module.
- **README**: Rewritten — web-only product, Flask as a prerequisite, correct run command; removes the Windows-desktop / console-menu / no-external-packages claims.
- **ADR**: A new ADR (number 0002) records that the web UI replaces the console UI as the sole interface.
- **Glossary**: CONTEXT.md is unchanged — the web UI is presentation, not domain vocabulary.
- **Persistence**: Unchanged, per ADR 0001 (SQLite); no schema changes.

## Testing Decisions

- **Good tests assert external behavior only**: HTTP status codes, redirect targets, and the presence of layout elements (menu bar, logo, stylesheet link, footer, breadcrumbs, status badges) in rendered HTML. No assertions on internal template structure or CSS internals.
- **Single seam**: The Flask test client is the one seam for all new behavior — every route is exercised through it, matching the existing web tests. No new seams are introduced.
- **Modules tested**: The web app module (all routes, including the new layout assertions); the database module (its existing tests move with it, unchanged); the service layer is untouched and its tests stand.
- **Prior art**: The existing web tests already assert on rendered bytes via the test client against a temp-file SQLite database; the new layout assertions follow that exact pattern.
- **Adapter**: The Azure adapter stub has no behavior to test directly; it is exercised indirectly by the existing sync route test.
- **Isolation**: Unchanged — temp-file SQLite per test (a plain in-memory DB cannot be used because the service opens a fresh connection per operation).

## Out of Scope

- Real Azure DevOps sync logic (the adapter remains a stub).
- Authentication or authorization.
- Edit and delete operations for Epics, Features, and Stories (the UI remains create + browse).
- Status transitions in the UI (Status is displayed, not changed).
- Search and Dutch localization.
- JavaScript of any kind (no hamburger menu, no client-side behavior).
- Mobile-specific design beyond flex-wrap.
- Domain model or persistence schema changes.

## Further Notes

- The CBS design tokens in this spec were extracted from cbs.nl's production stylesheet; the zeroheight style-guide page is JS-rendered and its content API is not publicly fetchable. The token values above are the source of truth for the stylesheet.
- Akko and Soho are commercial fonts; we reference CBS's own CDN copies rather than self-hosting, with a system fallback.
- The earlier web spec positioned the console UI and web UI as coexisting; this spec supersedes that positioning — the web UI is now the sole interface (see ADR 0002).
- The repo has no packaging metadata, so the README run command must be verified against how the package is actually importable (likely a PYTHONPATH or working-directory requirement) at implementation time.
