"""
Service layer for PM Buddy.

Provides a thin abstraction over the DB class so that web routes can be decoupled from persistence details.
"""

from pathlib import Path
from typing import List, Optional

from .app import DB, Epic, Feature, Story, Status

class PMBuddyService:
    """
    Encapsulates business logic and data access.

    Parameters:
        db_path: Optional[Path] – path to the SQLite database.
            If None, a file‑based DB is created at ``pm_buddy.db``.
    """

    def __init__(self, db_path: Optional[Path] = None):
        # Store the database path. A new DB connection will be created for each operation to avoid SQLite thread‑safety issues.
        self.db_path = db_path if db_path else Path("pm_buddy.db")

    # Epic operations -----------------------------------------------------
    def add_epic(self, title: str, description: str = "") -> int:
        epic = Epic(title=title, description=description, status=Status.TODO)
        db = DB(db_path=self.db_path)
        return db.add_epic(epic)

    def list_epics(self) -> List[Epic]:
        db = DB(db_path=self.db_path)
        return db.list_epics()

    # Feature operations ---------------------------------------------------
    def add_feature(self, epic_id: int, title: str, description: str = "") -> int:
        feature = Feature(title=title, description=description, status=Status.TODO)
        db = DB(db_path=self.db_path)
        return db.add_feature(epic_id, feature)

    def list_features(self, epic_id: int) -> List[Feature]:
        db = DB(db_path=self.db_path)
        return db.list_features(epic_id)

    # Story operations -----------------------------------------------------
    def add_story(self, feature_id: int, title: str, description: str = "") -> int:
        story = Story(title=title, description=description)
        db = DB(db_path=self.db_path)
        return db.add_story(feature_id, story)

    def list_stories(self, feature_id: int) -> List[Story]:
        db = DB(db_path=self.db_path)
        return db.list_stories(feature_id)
