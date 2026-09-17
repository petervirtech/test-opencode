"""
SQLite persistence for PM Buddy.
"""

import sqlite3
from pathlib import Path
from typing import List

from .models import Epic, Feature, Story, Status

DB_PATH = Path("pm_buddy.db")


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
        assert cur.lastrowid is not None
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
        assert cur.lastrowid is not None
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
        assert cur.lastrowid is not None
        return cur.lastrowid

    def list_stories(self, feature_id: int) -> List[Story]:
        cur = self.conn.cursor()
        cur.execute("SELECT id, feature_id, title, description, status FROM stories WHERE feature_id = ?", (feature_id,))
        rows = cur.fetchall()
        return [Story(id=r[0], feature_id=r[1], title=r[2], description=r[3], status=Status(r[4])) for r in rows]
