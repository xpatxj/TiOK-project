import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from unittest.mock import patch
from main import app
from repository import get_posts, get_post, get_albums, get_photos
import coverage

class TestContract(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    @patch('repository.get_posts')
    def test_home(self, mock_get_posts):
        mock_get_posts.return_value = [{'id': 1, 'title': 'Test Post'}]
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Post', response.data)

    @patch('repository.get_post')
    def test_post(self, mock_get_post):
        mock_get_post.return_value = {
            'post': {'id': 1, 'title': 'Test Post'},
            'user': {'id': 1, 'name': 'Test User'},
            'comments': [{'id': 1, 'name': 'Test Comment'}]
        }
        response = self.client.get('/post/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Post', response.data)
        self.assertIn(b'Test User', response.data)
        self.assertIn(b'Test Comment', response.data)

    @patch('repository.get_albums')
    def test_albums(self, mock_get_albums):
        mock_get_albums.return_value = [{'id': 1, 'title': 'Test Album'}]
        response = self.client.get('/albums/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Album', response.data)

    @patch('repository.get_photos')
    def test_photos(self, mock_get_photos):
        mock_get_photos.return_value = [{'id': 1, 'title': 'Test Photo'}]
        response = self.client.get('/albums/1/photos')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Photo', response.data)

    @patch('repository.get_post')
    def test_post_not_found(self, mock_get_post):
        mock_get_post.return_value = {}
        response = self.client.get('/post/999')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Post not found', response.data)

    @patch('repository.get_albums')
    def test_albums_not_found(self, mock_get_albums):
        mock_get_albums.return_value = []
        response = self.client.get('/albums/')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'No albums found', response.data)

    @patch('repository.get_photos')
    def test_photos_not_found(self, mock_get_photos):
        mock_get_photos.return_value = []
        response = self.client.get('/albums/999/photos')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'No photos found', response.data)
        
if __name__ == '__main__':
    unittest.main()
