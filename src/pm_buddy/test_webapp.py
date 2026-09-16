import unittest
from pathlib import Path
import pm_buddy.webapp as w
from pm_buddy.service import PMBuddyService

class TestPMBuddyWeb(unittest.TestCase):
    def setUp(self):
        # Use in-memory DB for web service
        w.service = PMBuddyService(db_path=Path(":memory:"))
        w.app.config['TESTING'] = True
        self.client = w.app.test_client()
    
    def test_index_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # Should contain the title header
        self.assertIn(b'PM Buddy', response.data)
    
    def test_add_epic(self):
        # POST to add epic
        response = self.client.post('/add_epic', data={'title': 'Test Epic', 'description':'desc'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # After redirect, epic should appear in list
        self.assertIn(b'Test Epic', response.data)

if __name__ == '__main__':
    unittest.main()
