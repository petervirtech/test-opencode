import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pm_buddy.webapp as w
from pm_buddy.service import PMBuddyService
from pm_buddy.test_support import TempDB


class TestPMBuddyWeb(unittest.TestCase):
    def setUp(self):
        self.db = TempDB()
        w.service = PMBuddyService(db_path=self.db.path)
        w.app.config['TESTING'] = True
        self.client = w.app.test_client()

    def tearDown(self):
        self.db.close()

    def test_index_get_lists_epics(self):
        w.service.add_epic("Test Epic")
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'PM Buddy', response.data)
        self.assertIn(b'Test Epic', response.data)

    def test_add_epic_redirects_to_index(self):
        response = self.client.post('/add_epic', data={'title': 'Test Epic'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers['Location'], '/')

    def test_add_epic_appears_in_list_after_redirect(self):
        response = self.client.post(
            '/add_epic', data={'title': 'Test Epic', 'description': 'desc'},
            follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Epic', response.data)

    def test_epic_detail_shows_features(self):
        eid = w.service.add_epic("Epic Alpha")
        w.service.add_feature(eid, "Feature One")
        response = self.client.get(f'/epic/{eid}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Epic Alpha', response.data)
        self.assertIn(b'Feature One', response.data)

    def test_add_feature_redirects_to_epic(self):
        eid = w.service.add_epic("Epic")
        response = self.client.post(f'/add_feature/{eid}', data={'title': 'Feature One'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers['Location'], f'/epic/{eid}')
        response = self.client.get(f'/epic/{eid}')
        self.assertIn(b'Feature One', response.data)

    def test_feature_detail_shows_stories(self):
        eid = w.service.add_epic("Epic Alpha")
        fid = w.service.add_feature(eid, "Feature Beta")
        w.service.add_story(fid, "Story One")
        response = self.client.get(f'/feature/{fid}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Feature Beta', response.data)
        self.assertIn(b'Story One', response.data)

    def test_add_story_redirects_to_feature(self):
        eid = w.service.add_epic("Epic")
        fid = w.service.add_feature(eid, "Feature")
        response = self.client.post(f'/add_story/{fid}', data={'title': 'Story One'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers['Location'], f'/feature/{fid}')
        response = self.client.get(f'/feature/{fid}')
        self.assertIn(b'Story One', response.data)

    def test_sync_redirects_to_index(self):
        response = self.client.get('/sync')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers['Location'], '/')


if __name__ == '__main__':
    unittest.main()
