"""
Domain model for PM Buddy.

Mid-level backlog structure: Epic -> Feature -> Story.
Each entity has a title, description and status.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class Status(Enum):
    TODO = "To Do"
    IN_PROGRESS = "In Progress"
    DONE = "Done"


@dataclass
class Story:
    id: Optional[int] = None
    feature_id: Optional[int] = None
    title: str = ""
    description: str = ""
    status: Status = Status.TODO


@dataclass
class Feature:
    id: Optional[int] = None
    epic_id: Optional[int] = None
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
