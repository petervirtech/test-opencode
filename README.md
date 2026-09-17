# PM Buddy

A lightweight product‑manager companion for the web. Browse and build a mid‑level backlog — **Epics → Features → User Stories** — in a CBS‑branded interface.

## Features
- Manage a mid‑level backlog: **Epics → Features → User Stories**.
- Persist data locally in an SQLite database (`pm_buddy.db`).
- Web UI styled with the CBS design system (brand colors, Akko/Soho typography).
- Stub Azure DevOps (TFS) adapter – ready to extend with sync logic.

## Prerequisites
- Python 3.8+
- Flask (`pip install flask`)

## Installation
Clone the repo and install the one external dependency into a virtual environment:

```bash
git clone https://github.com/petervirtech/test-opencode.git
cd test-opencode
python -m venv .venv
.venv/bin/pip install flask
```

The SQLite database is created automatically on first run.

## Running the Application
The package lives in `src/` and is not installed, so put it on the path:

```bash
PYTHONPATH=src .venv/bin/python -m pm_buddy.webapp
```

Then open <http://127.0.0.1:5000> in a browser. Use the menu bar to browse Epics, add Epics/Features/Stories, and trigger the (stub) Azure sync.

## Running Tests
```bash
PYTHONPATH=src .venv/bin/python -m unittest discover -s src/pm_buddy -p 'test_*.py'
```
All tests should pass.

## Contributing
Feel free to fork, create issues or pull requests. The repo follows PEP‑8 and uses type hints.

## License
MIT – see the LICENSE file (not included in this snippet).
