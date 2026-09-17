You are a coding assistant. Provide concise, direct answers. 
Do NOT show your reasoning process. Skip intermediate steps.
Only output the final code or answer.

## Commands

A `.venv` with flask and mypy already exists — use it; the README's setup steps are already done. The package is not installed, so put `src` on the path (README has the run/test commands).

- Typecheck: `PYTHONPATH=src .venv/bin/python -m mypy src/pm_buddy --ignore-missing-imports` (no mypy config in the repo; the flag is required)

## Gotchas

- Running the app from the repo root mutates the tracked `pm_buddy.db`; run it from a scratch directory instead.
- The web UI is zero-JS by design; keep it that way (no client-side behavior, no hamburger menu).
- CBS design tokens live in `src/pm_buddy/static/cbs.css` as custom properties; the values were extracted from cbs.nl's production stylesheet and are the source of truth (the zeroheight style-guide page is JS-rendered and not fetchable). Akko/Soho fonts are referenced from CBS's CDN, never self-hosted.
- Status is display-only: no transition operations exist (items are created To Do); tests seed non-default values via raw SQL (`test_webapp._set_status`).

## Agent skills

### Issue tracker
Local Markdown. See `docs/agents/issue-tracker.md`.

### Domain docs
Single-context layout. See `docs/agents/domain.md`.