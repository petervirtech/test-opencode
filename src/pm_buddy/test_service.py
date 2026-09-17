import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pm_buddy.service import PMBuddyService
from pm_buddy.test_support import TempDB


class TestPMBuddyService(unittest.TestCase):
    def setUp(self):
        self.db = TempDB()
        self.service = PMBuddyService(db_path=self.db.path)

    def tearDown(self):
        self.db.close()

    def test_add_and_list_epic(self):
        eid = self.service.add_epic("Test Epic", "desc")
        epics = self.service.list_epics()
        self.assertEqual(len(epics), 1)
        self.assertEqual(epics[0].id, eid)
        self.assertEqual(epics[0].title, "Test Epic")
        self.assertEqual(epics[0].description, "desc")

    def test_add_feature_and_list_features(self):
        eid = self.service.add_epic("Epic")
        fid = self.service.add_feature(eid, "Feature", "fdesc")
        features = self.service.list_features(eid)
        self.assertEqual(len(features), 1)
        self.assertEqual(features[0].id, fid)
        self.assertEqual(features[0].title, "Feature")
        self.assertEqual(features[0].epic_id, eid)

    def test_add_story_and_list_stories(self):
        eid = self.service.add_epic("Epic")
        fid = self.service.add_feature(eid, "Feature")
        sid = self.service.add_story(fid, "Story", "sdesc")
        stories = self.service.list_stories(fid)
        self.assertEqual(len(stories), 1)
        self.assertEqual(stories[0].id, sid)
        self.assertEqual(stories[0].title, "Story")
        self.assertEqual(stories[0].feature_id, fid)

    def test_ids_are_persisted_across_connections(self):
        eid = self.service.add_epic("Epic")
        fid = self.service.add_feature(eid, "Feature")
        sid = self.service.add_story(fid, "Story")
        # A fresh service instance over the same database sees the same rows.
        other = PMBuddyService(db_path=self.db.path)
        self.assertEqual(other.list_epics()[0].id, eid)
        self.assertEqual(other.list_features(eid)[0].id, fid)
        self.assertEqual(other.list_stories(fid)[0].id, sid)


if __name__ == '__main__':
    unittest.main()
