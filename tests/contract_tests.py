import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from unittest.mock import patch
from main import app
import requests
from repository import get_posts, get_post, get_albums, get_photos

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

    def test_remote_get_posts(self):
        expected_post_id1 = {
            "userId": 1,
            "id": 1,
            "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
        }
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json; charset=utf-8"
        posts = response.json()
        assert posts[0] == expected_post_id1

    def test_remote_get_post(self):
        expected_post_id1 = {
            "userId": 1,
            "id": 1,
            "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
        }
        response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json; charset=utf-8"
        post = response.json()
        assert post == expected_post_id1

    def test_remote_get_user(self):
        expected_user_id1 = {
            "id": 1,
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "Sincere@april.biz",
            "address": {
                "street": "Kulas Light",
                "suite": "Apt. 556",
                "city": "Gwenborough",
                "zipcode": "92998-3874",
                "geo": {
                    "lat": "-37.3159",
                    "lng": "81.1496"
                }
            },
            "phone": "1-770-736-8031 x56442",
            "website": "hildegard.org",
            "company": {
                "name": "Romaguera-Crona",
                "catchPhrase": "Multi-layered client-server neural-net",
                "bs": "harness real-time e-markets"
            }
        }
        response = requests.get('https://jsonplaceholder.typicode.com/users/1')
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json; charset=utf-8"
        user = response.json()
        assert user == expected_user_id1

    def test_remote_get_comment(self):
        expected_comment_id1 = {
            "postId": 1,
            "id": 1,
            "name": "id labore ex et quam laborum",
            "email": "Eliseo@gardner.biz",
            "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
        }
        response = requests.get('https://jsonplaceholder.typicode.com/comments/1')
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json; charset=utf-8"
        comment = response.json()
        assert comment == expected_comment_id1

    def test_remote_get_album(self):
        expected_album_id1 = {
            "userId": 1,
            "id": 1,
            "title": "quidem molestiae enim"
        }
        response = requests.get('https://jsonplaceholder.typicode.com/albums/1')
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json; charset=utf-8"
        album = response.json()
        assert album == expected_album_id1

    def test_remote_get_photos(self):
        expected_photo_id1 = {
            "albumId": 1,
            "id": 1,
            "title": "accusamus beatae ad facilis cum similique qui sunt",
            "url": "https://via.placeholder.com/600/92c952",
            "thumbnailUrl": "https://via.placeholder.com/150/92c952"
        }
        response = requests.get('https://jsonplaceholder.typicode.com/photos')
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json; charset=utf-8"
        photos = response.json()
        assert photos[0] == expected_photo_id1

    @patch('repository.get_posts_range')
    def test_filter_posts(self, mock_get_posts_range):
        mock_get_posts_range.return_value = [{'id': 1, 'title': 'Test Post', 'body': 'Test Body'}]
        response = self.client.post('/filter', data={'range_left': '0', 'range_right': '10'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Post', response.data)

    @patch('repository.get_posts_range')
    def test_filter_posts_invalid_range(self, mock_get_posts_range):
        mock_get_posts_range.return_value = []
        response = self.client.post('/filter', data={'range_left': 'a', 'range_right': 'b'})
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Test Post', response.data)

    def test_filter_posts_invalid_method(self):
        response = self.client.get('/filter')
        self.assertEqual(response.status_code, 405)

    @patch('repository.get_posts_range')
    def test_filter_posts_server_error(self, mock_get_posts_range):
        mock_get_posts_range.side_effect = Exception('Server error')
        response = self.client.post('/filter', data={'range_left': '0', 'range_right': '10'})
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Error: Server error', response.data)

if __name__ == '__main__':
    unittest.main()
