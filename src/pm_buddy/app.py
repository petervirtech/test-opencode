"""
Simple Product Manager Buddy.

Provides a console UI to manage Epics, Features and User Stories in an SQLite database.
The data model is mid‑level: Epic -> Feature -> Story. Each entity has a title, description and status.

A hybrid Azure DevOps adapter is included but only contains stubs – it can be extended to sync with TFS.
"""

import sqlite3
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Optional

DB_PATH = Path("pm_buddy.db")

# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------
@dataclass
class Story:
    id: Optional[int] = None
    title: str = ""
    description: str = ""
    status: str = "To Do"

@dataclass
class Feature:
    id: Optional[int] = None
    title: str = ""
    description: str = ""
    status: str = "To Do"
    stories: List[Story] = field(default_factory=list)

@dataclass
class Epic:
    id: Optional[int] = None
    title: str = ""
    description: str = ""
    status: str = "To Do"
    features: List[Feature] = field(default_factory=list)

# ---------------------------------------------------------------------------
# Database helpers
# ---------------------------------------------------------------------------
class DB:
    def __init__(self, db_path: Path = DB_PATH):
        self.conn = sqlite3.connect(db_path)
        self._create_tables()

    def _create_tables(self):
        cur = self.conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS epics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                status TEXT
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS features (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                epic_id INTEGER,
                title TEXT NOT NULL,
                description TEXT,
                status TEXT,
                FOREIGN KEY(epic_id) REFERENCES epics(id)
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS stories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                feature_id INTEGER,
                title TEXT NOT NULL,
                description TEXT,
                status TEXT,
                FOREIGN KEY(feature_id) REFERENCES features(id)
            );
        """)
        self.conn.commit()

    # CRUD for Epics -------------------------------------------------------
    def add_epic(self, epic: Epic) -> int:
        cur = self.conn.cursor()
        cur.execute("INSERT INTO epics (title, description, status) VALUES (?, ?, ?)",
                    (epic.title, epic.description, epic.status))
        self.conn.commit()
        return cur.lastrowid

    def list_epics(self) -> List[Epic]:
        cur = self.conn.cursor()
        cur.execute("SELECT id, title, description, status FROM epics")
        rows = cur.fetchall()
        return [Epic(id=r[0], title=r[1], description=r[2], status=r[3]) for r in rows]

    # Similar CRUD methods can be added for Feature and Story.

# ---------------------------------------------------------------------------
# Azure DevOps adapter (hybrid stub)
# ---------------------------------------------------------------------------
class AzureAdapter:
    def __init__(self, db: DB):
        self.db = db
        # In a real implementation we would store credentials and endpoints.

    def sync_to_azure(self):
        """
        Placeholder for hybrid sync logic.
        Would iterate over local entities, compare with Azure DevOps work items,
        create or update as necessary.
        """
        pass

    def sync_from_azure(self):
        """
        Placeholder for pulling latest state from Azure DevOps.
        """
        pass

# ---------------------------------------------------------------------------
# Simple console UI
# ---------------------------------------------------------------------------
def main():
    db = DB()
    while True:
        print("\nPM Buddy Menu")
        print("1. List Epics")
        print("2. Add Epic")
        print("3. Exit")
        choice = input("Select: ")
        if choice == "1":
            epics = db.list_epics()
            for e in epics:
                print(f"{e.id}: {e.title} [{e.status}]")
        elif choice == "2":
            title = input("Epic title: ")
            desc = input("Description (optional): ")
            epic = Epic(title=title, description=desc)
            eid = db.add_epic(epic)
            print(f"Epic {eid} created.")
        elif choice == "3":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
