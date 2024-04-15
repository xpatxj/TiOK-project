import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import repository
import unittest
from unittest.mock import patch, MagicMock

class TestRepository(unittest.TestCase):

    # Test długości listy postów
    @patch('requests.get')
    def test_posts_length(self, mock_get):
        mock_get.return_value.json.return_value = [{} for _ in range(100)] # zwraca 100 postów do testowania
        posts = repository.get_posts()
        self.assertEqual(len(posts), 100)

    # Test długości listy albumów
    @patch('requests.get')
    def test_albums_length(self, mock_get):
        mock_get.return_value.json.return_value = [{} for _ in range(100)]  
        albums = repository.get_albums()
        self.assertEqual(len(albums), 100)

    # Test istnienia postu
    @patch('requests.get')
    def test_post_exists(self, mock_get):
        mock_get.return_value.json.return_value = {"userId": 1, "id": 1, "title": "Test Post", "body": "Test Body"}  
        post = repository.get_post(1)
        self.assertNotEqual(len(post), 0)

    # Test struktury postu
    @patch('requests.get')
    def test_post_structure(self, mock_get):
        mock_get.return_value.json.return_value = {"userId": 1, "id": 1, "title": "Test Post", "body": "Test Body"}  
        post = repository.get_post(1)
        self.assertNotEqual(len(post["user"]), 0)
        self.assertNotEqual(len(post["comments"]), 0)

    # Test złego ID postu
    @patch('requests.get')
    def test_post_with_wrong_id(self, mock_get):
        mock_get.return_value.json.return_value = {}
        post = repository.get_post("niepoprawny argument")
        self.assertEqual(len(post), 0)

    # Test niestniejącego ID postu
    @patch('requests.get')
    def test_post_with_not_existing_id(self, mock_get):
        mock_get.return_value.json.return_value = {} 
        post = repository.get_post(-1)
        self.assertEqual(len(post), 0)

    # Test długości listy zdjęć
    @patch('requests.get')
    def test_photos_length(self, mock_get):
        mock_get.return_value.json.return_value = [{} for _ in range(10)] 
        photos = repository.get_photos(1)
        self.assertNotEqual(len(photos), 0)

    # Test złego ID zdjęć
    @patch('requests.get')
    def test_photos_with_wrong_id(self, mock_get):
        mock_get.return_value.json.return_value = [] 
        photo = repository.get_photos("niepoprawny argument")
        self.assertEqual(len(photo), 0)

    # Test niestniejącego ID zdjęć
    @patch('requests.get')
    def test_photos_with_not_existing_id(self, mock_get):
        mock_get.return_value.json.return_value = []  
        photo = repository.get_photos(-1)
        self.assertEqual(len(photo), 0)

    # Test istnienia zdjęć
    @patch('requests.get')
    def test_get_photos_non_empty(self, mock_get):
        mock_get.return_value.json.return_value = [{"id": 1, "title": "Test Photo", "url": "http://example.com/photo.jpg", "thumbnailUrl": "http://example.com/thumbnail.jpg"} for _ in range(10)]
        photos = repository.get_photos(1)
        self.assertTrue(all(len(photo) > 0 for photo in photos))

    # Test istnienia kluczy w postach
    @patch('requests.get')
    def test_get_post_keys(self, mock_get):
        mock_get.return_value.json.return_value = {"userId": 1, "id": 1, "title": "Test Post", "body": "Test Body"}  
        post = repository.get_post(1)
        self.assertIn("post", post)
        self.assertIn("user", post)
        self.assertIn("comments", post)

    # Test typu postu
    @patch('requests.get')
    def test_get_post_type(self, mock_get):
        mock_get.return_value.json.return_value = {"userId": 1, "id": 1, "title": "Test Post", "body": "Test Body"} 
        post = repository.get_post(1)
        self.assertIsInstance(post, dict)

    # Test typu albumu
    @patch('requests.get')
    def test_get_albums_type(self, mock_get):
        mock_get.return_value.json.return_value = [{} for _ in range(100)] 
        albums = repository.get_albums()
        self.assertIsInstance(albums, list)

    # Test typu zdjęć
    @patch('requests.get')
    def test_get_photos_type(self, mock_get):
        mock_get.return_value.json.return_value = [{} for _ in range(10)] 
        photos = repository.get_photos(1)
        self.assertIsInstance(photos, list)

    # Test istnienia klucza usera
    @patch('requests.get')
    def test_get_post_user_keys(self, mock_get):
        mock_get.return_value.json.return_value = {"userId": 1, "id": 1, "title": "Test Post", "body": "Test Body"}
        post = repository.get_post(1)
        self.assertIn("id", post["user"])

    # Test istnienia klucza w zdjęciach
    @patch('requests.get')
    def test_get_photos_keys(self, mock_get):
        mock_get.return_value.json.return_value = [{"id": 1, "title": "Test Photo", "url": "http://example.com/photo.jpg", "thumbnailUrl": "http://example.com/thumbnail.jpg"} for _ in range(10)]  # return 10 photos for testing
        photos = repository.get_photos(1)
        for photo in photos:
            self.assertIn("id", photo)
            self.assertIn("title", photo)
            self.assertIn("url", photo)
            self.assertIn("thumbnailUrl", photo)

    # Test istnienia kluczy w komentarzach
    @patch('requests.get')
    def test_get_post_comments_keys(self, mock_get):
        mock_responses = [
            {"userId": 1, "id": 1, "title": "Test Post", "body": "Test Body"},  # post
            {"id": 1, "name": "Test User", "username": "testuser"},  # user
            [{"id": 1, "name": "Test Comment", "email": "test@example.com"}]  # comments
        ]

        mock_get.side_effect = [MagicMock(json=MagicMock(return_value=response)) for response in mock_responses]

        post = repository.get_post(1)

        for comment in post["comments"]:
            self.assertIn("id", comment)
            self.assertIn("name", comment)
            self.assertIn("email", comment)

if __name__ == '__main__':
    unittest.main()
