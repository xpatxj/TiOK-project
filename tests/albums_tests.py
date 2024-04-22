import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from unittest.mock import patch, MagicMock
from flask import g
from main import app 

class TestAlbums(unittest.TestCase):

    # Ustawianie aplikacji
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    # Testowanie złego routingu /albums/
    @patch('repository.get_albums')
    def test_albums_route(self, mock_get_albums):
        mock_get_albums.return_value = []  # zwraca pustą listę albumów do testowania
        with self.app.app_context():
            response = self.client.get('/albums/')
            self.assertEqual(response.status_code, 404)
            mock_get_albums.assert_called_once()

    # Testowanie routingu albums
    @patch('repository.get_albums')
    def test_albums_route_with_albums(self, mock_get_albums):
        mock_get_albums.return_value = [{'id': 1, 'title': 'Test Album'}]
        with self.app.app_context():
            response = self.client.get('/albums/')
            self.assertEqual(response.status_code, 200)
            mock_get_albums.assert_called_once()

    # Testowanie routingu zdjęcia
    @patch('repository.get_photos')
    def test_photos_route_with_photos(self, mock_get_photos):
        mock_get_photos.return_value = [{'id': 1, 'title': 'Test Photo', 'url': 'http://example.com/photo.jpg'}]
        with self.app.app_context():
            response = self.client.get('/albums/1/photos')
            self.assertEqual(response.status_code, 200)
            mock_get_photos.assert_called_once_with('1')

    # Testowanie routingu zdjęcia z niepoprawnym ID albumu
    @patch('repository.get_photos')
    def test_photos_route_with_invalid_album_id(self, mock_get_photos):
        mock_get_photos.return_value = []
        with self.app.app_context():
            response = self.client.get('/albums/999/photos')  
            self.assertEqual(response.status_code, 404)
            mock_get_photos.assert_called_once_with('999')


if __name__ == '__main__':
    unittest.main()
