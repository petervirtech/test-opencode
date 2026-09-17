import sqlite3
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

    def test_index_shows_menu_bar_with_logo_and_nav(self):
        response = self.client.get('/')
        self.assert_layout(response)
        data = response.data
        self.assertIn(b'Epics', data)
        self.assertIn(b'Sync', data)

    def test_index_logo_links_to_epic_list(self):
        response = self.client.get('/')
        self.assertIn(b'<a class="logo" href="/">', response.data)

    def test_index_highlights_current_section(self):
        response = self.client.get('/')
        self.assertIn(b'<a href="/" class="active">Epics</a>', response.data)

    def test_index_links_stylesheet(self):
        response = self.client.get('/')
        self.assertIn(b'<link rel="stylesheet" href="/static/cbs.css">', response.data)

    def test_index_shows_footer(self):
        response = self.client.get('/')
        data = response.data
        self.assertIn(b'<footer class="site-footer">', data)
        self.assertIn(b'your product management companion', data)

    def assert_layout(self, response):
        self.assertEqual(response.status_code, 200)
        data = response.data
        self.assertIn(b'<header class="menu-bar">', data)
        self.assertIn(b'/static/cbs-logo.svg', data)
        self.assertIn(b'<link rel="stylesheet" href="/static/cbs.css">', data)
        self.assertIn(b'<footer class="site-footer">', data)

    def test_add_epic_page_has_layout(self):
        self.assert_layout(self.client.get('/add_epic'))

    def test_epic_detail_page_has_layout(self):
        eid = w.service.add_epic("Epic Alpha")
        self.assert_layout(self.client.get(f'/epic/{eid}'))

    def test_add_feature_page_has_layout(self):
        eid = w.service.add_epic("Epic")
        self.assert_layout(self.client.get(f'/add_feature/{eid}'))

    def test_feature_detail_page_has_layout(self):
        eid = w.service.add_epic("Epic")
        fid = w.service.add_feature(eid, "Feature")
        self.assert_layout(self.client.get(f'/feature/{fid}'))

    def test_add_story_page_has_layout(self):
        eid = w.service.add_epic("Epic")
        fid = w.service.add_feature(eid, "Feature")
        self.assert_layout(self.client.get(f'/add_story/{fid}'))

    def test_index_renders_add_epic_as_button(self):
        response = self.client.get('/')
        self.assertIn(b'<a class="btn" href="/add_epic">Add Epic</a>', response.data)

    def test_epic_detail_renders_add_feature_as_button(self):
        eid = w.service.add_epic("Epic")
        response = self.client.get(f'/epic/{eid}')
        self.assertIn(b'<a class="btn" href="/add_feature/' + str(eid).encode() + b'">Add Feature</a>', response.data)

    def test_feature_detail_renders_add_story_as_button(self):
        eid = w.service.add_epic("Epic")
        fid = w.service.add_feature(eid, "Feature")
        response = self.client.get(f'/feature/{fid}')
        self.assertIn(b'<a class="btn" href="/add_story/' + str(fid).encode() + b'">Add Story</a>', response.data)

    def assert_form_fields(self, response):
        data = response.data
        self.assertIn(b'class="form-control"', data)
        self.assertIn(b'<button type="submit" class="btn">', data)

    def test_add_epic_page_styles_form_fields(self):
        self.assert_form_fields(self.client.get('/add_epic'))

    def test_add_feature_page_styles_form_fields(self):
        eid = w.service.add_epic("Epic")
        self.assert_form_fields(self.client.get(f'/add_feature/{eid}'))

    def test_add_story_page_styles_form_fields(self):
        eid = w.service.add_epic("Epic")
        fid = w.service.add_feature(eid, "Feature")
        self.assert_form_fields(self.client.get(f'/add_story/{fid}'))

    def _set_status(self, table: str, item_id: int, status: str):
        # No API exists to change Status (display-only), so seed the value directly.
        conn = sqlite3.connect(self.db.path)
        try:
            conn.execute(f"UPDATE {table} SET status = ? WHERE id = ?", (status, item_id))
            conn.commit()
        finally:
            conn.close()

    def test_epic_detail_shows_breadcrumb(self):
        eid = w.service.add_epic("Epic Alpha")
        response = self.client.get(f'/epic/{eid}')
        data = response.data
        self.assertIn(b'<nav class="breadcrumbs"', data)
        self.assertIn(b'&rsaquo;', data)
        self.assertIn(b'Epic Alpha', data)

    def test_feature_detail_shows_breadcrumb(self):
        eid = w.service.add_epic("Epic Alpha")
        fid = w.service.add_feature(eid, "Feature Beta")
        response = self.client.get(f'/feature/{fid}')
        data = response.data
        self.assertIn(b'<nav class="breadcrumbs"', data)
        self.assertIn(b'&rsaquo;', data)
        self.assertIn(b'Epic Alpha', data)
        self.assertIn(b'Feature Beta', data)

    def test_epic_detail_shows_status_badge(self):
        eid = w.service.add_epic("Epic Alpha")
        response = self.client.get(f'/epic/{eid}')
        self.assertIn(b'<span class="badge badge-to-do">To Do</span>', response.data)

    def test_feature_detail_shows_in_progress_badge(self):
        eid = w.service.add_epic("Epic")
        fid = w.service.add_feature(eid, "Feature Beta")
        self._set_status('features', fid, 'In Progress')
        response = self.client.get(f'/feature/{fid}')
        self.assertIn(b'<span class="badge badge-in-progress">In Progress</span>', response.data)

    def test_feature_detail_shows_done_badge(self):
        eid = w.service.add_epic("Epic")
        fid = w.service.add_feature(eid, "Feature Beta")
        self._set_status('features', fid, 'Done')
        response = self.client.get(f'/feature/{fid}')
        self.assertIn(b'<span class="badge badge-done">Done</span>', response.data)


if __name__ == '__main__':
    unittest.main()
