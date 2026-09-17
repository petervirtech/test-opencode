# 03: All remaining pages inherit the base layout

**What to build:** Every page in the app — add Epic, Epic detail, add Feature, Feature detail, add Story — renders inside the same boilerplate layout as the Epic list page, so navigating the whole app feels like one consistent CBS-branded product. Forms use design-token-styled fields and primary actions render as styled buttons. Demoable: click through the entire app; no page is left unstyled.

**Blocked by:** 02 (CBS boilerplate on the Epic list page)

**Status:** done

- [x] All five remaining pages inherit the base template and keep their page-specific content
- [x] No page renders without the menu bar, logo, or footer
- [x] Form fields and submit buttons are styled with the design tokens (control height, border radius)
- [x] Primary actions (Add Epic / Add Feature / Add Story) render as styled buttons
- [x] Web tests assert the layout elements on each of the five pages
