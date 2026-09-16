"""
Simple Product Manager Buddy.

Provides a console UI to manage Epics, Features and User Stories in an SQLite database.
The data model is mid‑level: Epic -> Feature -> Story. Each entity has a title, description and status.

A hybrid Azure DevOps adapter is included but only contains stubs – it can be extended to sync with TFS.
""

import sqlite3
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum

DB_PATH = Path("pm_buddy.db")

# ---------------------------------------------------------------------------
# Domain status enum
# ---------------------------------------------------------------------------
class Status(Enum):
    TODO = "To Do"
    IN_PROGRESS = "In Progress"
    DONE = "Done"

# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------
@dataclass
class Story:
    id: Optional[int] = None
    title: str = ""
    description: str = ""
    status: Status = Status.TODO

@dataclass
class Feature:
    id: Optional[int] = None
    title: str = ""
    description: str = ""
    status: Status = Status.TODO
    stories: List[Story] = field(default_factory=list)

@dataclass
class Epic:
    id: Optional[int] = None
    title: str = ""
    description: str = ""
    status: Status = Status.TODO
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
                    (epic.title, epic.description, epic.status.value))
        self.conn.commit()
        return cur.lastrowid

    def list_epics(self) -> List[Epic]:
        cur = self.conn.cursor()
        cur.execute("SELECT id, title, description, status FROM epics")
        rows = cur.fetchall()
        return [Epic(id=r[0], title=r[1], description=r[2], status=Status(r[3])) for r in rows]

    # CRUD for Features -----------------------------------------------------
    def add_feature(self, epic_id: int, feature: Feature) -> int:
        cur = self.conn.cursor()
        cur.execute("INSERT INTO features (epic_id, title, description, status) VALUES (?, ?, ?, ?)",
                    (epic_id, feature.title, feature.description, feature.status.value))
        self.conn.commit()
        return cur.lastrowid

    def list_features(self, epic_id: int) -> List[Feature]:
        cur = self.conn.cursor()
        cur.execute("SELECT id, epic_id, title, description, status FROM features WHERE epic_id = ?", (epic_id,))
        rows = cur.fetchall()
        return [Feature(id=r[0], epic_id=r[1], title=r[2], description=r[3], status=Status(r[4])) for r in rows]

    # CRUD for Stories -----------------------------------------------------
    def add_story(self, feature_id: int, story: Story) -> int:
        cur = self.conn.cursor()
        cur.execute("INSERT INTO stories (feature_id, title, description, status) VALUES (?, ?, ?, ?)",
                    (feature_id, story.title, story.description, story.status.value))
        self.conn.commit()
        return cur.lastrowid

    def list_stories(self, feature_id: int) -> List[Story]:
        cur = self.conn.cursor()
        cur.execute("SELECT id, feature_id, title, description, status FROM stories WHERE feature_id = ?", (feature_id,))
        rows = cur.fetchall()
        return [Story(id=r[0], feature_id=r[1], title=r[2], description=r[3], status=Status(r[4])) for r in rows]

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
                print(f"{e.id}: {e.title} [{e.status.value}]")
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

if __name__ == '__main__':
    main()
