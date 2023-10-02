"""pages/tests.py"""
from django.test import SimpleTestCase


class SimpleTests(SimpleTestCase):
    """SimpleTests"""

    def test_home_page_status_code(self):
        """test_home_page_status_code"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        """test_about_page_status_code"""
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
