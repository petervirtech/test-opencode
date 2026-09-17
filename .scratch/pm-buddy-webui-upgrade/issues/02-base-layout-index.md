# 02: CBS boilerplate on the Epic list page

**What to build:** The Epic list page renders inside a shared boilerplate layout styled with the CBS design system: a white menu bar with the CBS logo (left, linking home) and Epics/Sync navigation (right, current section highlighted in brand indigo), a centered 1100px content area, and a minimal footer. Typography is Akko (text) and Soho (titles) via @font-face from the CBS CDN with a system fallback; all colors, spacing, and radii come from CBS design tokens as CSS custom properties in a single stylesheet. The logo is the real CBS SVG with a text wordmark fallback. Demoable: run the web app and the Epic list page looks like a CBS-branded product.

**Blocked by:** None (can start immediately)

**Status:** done

- [x] A single base template defines the layout (menu bar, content block, footer) and the Epic list page inherits from it
- [x] The menu bar shows the CBS logo linking to the Epic list, plus Epics and Sync links, with the current section highlighted
- [x] The menu bar wraps on narrow screens without JavaScript
- [x] A single stylesheet defines the CBS design tokens (brand #271d6c, blue #0058b8, text #091d23, grays, spacing scale, border radius) as custom properties
- [x] Akko and Soho load via @font-face from the CBS CDN with a system font fallback
- [x] The CBS logo is a static asset served by the web app, with a text fallback if the image is missing
- [x] The content area is centered with a 1100px max width
- [x] A minimal footer (app name plus tagline) renders on the page
- [x] Web tests assert the layout elements (menu bar, logo, stylesheet link, footer) on the Epic list page
