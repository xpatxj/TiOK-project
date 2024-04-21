import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from unittest.mock import patch, MagicMock
from flask import g
from main import app
import coverage

class TestPosts(unittest.TestCase):

    # Ustawianie aplikacji
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    # Testowanie routingu /
    @patch('repository.get_posts')
    def test_root_route(self, mock_get):
        mock_get.return_value = []  # zwraca pustą listę albumów do testowania
        with self.app.app_context():
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            mock_get.assert_called_once()

    # Testowanie routingu '/post/1'
    @patch('repository.get_post')
    def test_post_route(self, mock_get_albums):
        mock_get_albums.return_value.json.return_value = [{"post": {"id": 1, "title":"", "body": ""}, "user": {"id": 1, "name": ""}, "comments": []}]
        with self.app.app_context():
            response = self.client.get('/post/1')
            self.assertEqual(response.status_code, 200)
            mock_get_albums.assert_called_once()


    # Testowanie routingu postu z niepoprawnym ID
    @patch('repository.get_post')
    def test_post_route_with_invalid_id(self, mock_get):
        mock_get.return_value = {}
        with self.app.app_context():
            response = self.client.get('/post/999')
            self.assertEqual(response.status_code, 404)
            mock_get.assert_called_once_with('999')


if __name__ == '__main__':
    unittest.main()
