import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pm_buddy.app import DB, Epic

class TestPMBuddyDB(unittest.TestCase):
    def setUp(self):
        # Use in-memory SQLite for tests
        self.db = DB(db_path=Path(":memory:"))

    def test_add_and_list_epic(self):
        epic = Epic(title="Test Epic", description="desc")
        eid = self.db.add_epic(epic)
        epics = self.db.list_epics()
        self.assertEqual(len(epics), 1)
        self.assertEqual(epics[0].id, eid)
        self.assertEqual(epics[0].title, "Test Epic")

if __name__ == '__main__':
    unittest.main()

