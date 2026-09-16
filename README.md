# PM Buddy

A lightweight product‑manager companion that runs on Windows desktops with only Python available.

## Features
- Manage a mid‑level backlog: **Epics → Features → User Stories**.
- Persist data locally in an SQLite database (`pm_buddy.db`).
- Simple console UI for CRUD operations.
- Stub Azure DevOps (TFS) adapter – ready to extend with sync logic.

## Prerequisites
- Python 3.8+ (bundled with Windows). No external packages required.

## Installation
No installation is needed – just clone the repo and run the script. The SQLite database will be created automatically.

```bash
git clone https://github.com/petervirtech/test-opencode.git
cd test-opencode
python -m pm_buddy.app  # or python src/pm_buddy/app.py
```

## Running the Application
```bash
python -m pm_buddy.app
```
You will see a menu:
1. List Epics
2. Add Epic
3. Exit
Use the prompts to create and view backlog items.

## Running Tests
```bash
python -m unittest discover -s src/pm_buddy -p 'test_*.py'
```
All tests should pass.

## Contributing
Feel free to fork, create issues or pull requests. The repo follows PEP‑8 and uses type hints.

## License
MIT – see the LICENSE file (not included in this snippet).
