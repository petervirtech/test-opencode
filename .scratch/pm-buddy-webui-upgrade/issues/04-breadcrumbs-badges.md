# 04: Breadcrumbs and status badges on detail pages

**What to build:** On the Epic detail and Feature detail pages, the ad-hoc back links are replaced with breadcrumbs (Epics › Epic, and Epics › Epic › Feature), and each item's Status renders as a colored badge — To Do gray, In Progress blue, Done green — so hierarchy and state are scannable at a glance. Demoable: open any Feature detail page and see the full breadcrumb trail plus a colored status badge.

**Blocked by:** 03 (All remaining pages inherit the base layout)

**Status:** done

- [x] The Epic detail page shows an Epics › Epic breadcrumb
- [x] The Feature detail page shows an Epics › Epic › Feature breadcrumb
- [x] Status renders as a badge with the correct color per value (To Do gray, In Progress blue #0058b8, Done green #488225)
- [x] Web tests assert the breadcrumb and badge on both detail pages
