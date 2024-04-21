import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import repository
import unittest
from unittest.mock import patch, MagicMock
import coverage

class TestRepository(unittest.TestCase):

    #Przygotowanie fakeowych danych dla testow
    @classmethod
    def setUpClass(self):
        self.fake_albums = [{
            "userId": 1,
            "id": 1,
            "title": "quidem molestiae enim"
        },
            {
                "userId": 1,
                "id": 2,
                "title": "sunt qui excepturi placeat culpa"
            },
            {
                "userId": 1,
                "id": 3,
                "title": "omnis laborum odio"
            },
            {
                "userId": 1,
                "id": 4,
                "title": "non esse culpa molestiae omnis sed optio"
            },
            {
                "userId": 1,
                "id": 5,
                "title": "eaque aut omnis a"
            },
            {
                "userId": 1,
                "id": 6,
                "title": "natus impedit quibusdam illo est"
            },
            {
                "userId": 1,
                "id": 7,
                "title": "quibusdam autem aliquid et et quia"
            },
            {
                "userId": 1,
                "id": 8,
                "title": "qui fuga est a eum"
            },
            {
                "userId": 1,
                "id": 9,
                "title": "saepe unde necessitatibus rem"
            },
            {
                "userId": 1,
                "id": 10,
                "title": "distinctio laborum qui"
            }]

        self.fake_photos = [
            {
                "albumId": 1,
                "id": 1,
                "title": "accusamus beatae ad facilis cum similique qui sunt",
                "url": "https://via.placeholder.com/600/92c952",
                "thumbnailUrl": "https://via.placeholder.com/150/92c952"
            },
            {
                "albumId": 1,
                "id": 2,
                "title": "reprehenderit est deserunt velit ipsam",
                "url": "https://via.placeholder.com/600/771796",
                "thumbnailUrl": "https://via.placeholder.com/150/771796"
            },
            {
                "albumId": 1,
                "id": 3,
                "title": "officia porro iure quia iusto qui ipsa ut modi",
                "url": "https://via.placeholder.com/600/24f355",
                "thumbnailUrl": "https://via.placeholder.com/150/24f355"
            },
            {
                "albumId": 1,
                "id": 4,
                "title": "culpa odio esse rerum omnis laboriosam voluptate repudiandae",
                "url": "https://via.placeholder.com/600/d32776",
                "thumbnailUrl": "https://via.placeholder.com/150/d32776"
            },
            {
                "albumId": 1,
                "id": 5,
                "title": "natus nisi omnis corporis facere molestiae rerum in",
                "url": "https://via.placeholder.com/600/f66b97",
                "thumbnailUrl": "https://via.placeholder.com/150/f66b97"
            },
            {
                "albumId": 1,
                "id": 6,
                "title": "accusamus ea aliquid et amet sequi nemo",
                "url": "https://via.placeholder.com/600/56a8c2",
                "thumbnailUrl": "https://via.placeholder.com/150/56a8c2"
            },
            {
                "albumId": 1,
                "id": 7,
                "title": "officia delectus consequatur vero aut veniam explicabo molestias",
                "url": "https://via.placeholder.com/600/b0f7cc",
                "thumbnailUrl": "https://via.placeholder.com/150/b0f7cc"
            },
            {
                "albumId": 1,
                "id": 8,
                "title": "aut porro officiis laborum odit ea laudantium corporis",
                "url": "https://via.placeholder.com/600/54176f",
                "thumbnailUrl": "https://via.placeholder.com/150/54176f"
            },
            {
                "albumId": 1,
                "id": 9,
                "title": "qui eius qui autem sed",
                "url": "https://via.placeholder.com/600/51aa97",
                "thumbnailUrl": "https://via.placeholder.com/150/51aa97"
            },
            {
                "albumId": 1,
                "id": 10,
                "title": "beatae et provident et ut vel",
                "url": "https://via.placeholder.com/600/810b14",
                "thumbnailUrl": "https://via.placeholder.com/150/810b14"
            }]

        self.fake_posts = [
            {
                "userId": 1,
                "id": 1,
                "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
                "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
            },
            {
                "userId": 1,
                "id": 2,
                "title": "qui est esse",
                "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
            },
            {
                "userId": 1,
                "id": 3,
                "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
                "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
            },
            {
                "userId": 1,
                "id": 4,
                "title": "eum et est occaecati",
                "body": "ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit"
            },
            {
                "userId": 1,
                "id": 5,
                "title": "nesciunt quas odio",
                "body": "repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque"
            }]

        self.fake_users = [
            {
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
  },
            {
                "id": 2,
                "name": "Ervin Howell",
                "username": "Antonette",
                "email": "Shanna@melissa.tv",
                "address": {
                "street": "Victor Plains",
                "suite": "Suite 879",
                "city": "Wisokyburgh",
                "zipcode": "90566-7771",
                "geo": {
                "lat": "-43.9509",
                "lng": "-34.4618"
            }
    },
    "phone": "010-692-6593 x09125",
    "website": "anastasia.net",
    "company": {
      "name": "Deckow-Crist",
      "catchPhrase": "Proactive didactic contingency",
      "bs": "synergize scalable supply-chains"
    }
  },
            {
                "id": 3,
                "name": "Clementine Bauch",
                "username": "Samantha",
                "email": "Nathan@yesenia.net",
                "address": {
                "street": "Douglas Extension",
                "suite": "Suite 847",
                "city": "McKenziehaven",
                "zipcode": "59590-4157",
                "geo": {
                "lat": "-68.6102",
                "lng": "-47.0653"
            }
            },
    "phone": "1-463-123-4447",
    "website": "ramiro.info",
    "company": {
      "name": "Romaguera-Jacobson",
      "catchPhrase": "Face to face bifurcated interface",
      "bs": "e-enable strategic applications"
    }
  }]
        self.fake_comments=[
            {
                "postId": 1,
                "id": 1,
                "name": "id labore ex et quam laborum",
                "email": "Eliseo@gardner.biz",
                "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
            },
            {
                "postId": 1,
                "id": 2,
                "name": "quo vero reiciendis velit similique earum",
                "email": "Jayne_Kuhic@sydney.com",
                "body": "est natus enim nihil est dolore omnis voluptatem numquam\net omnis occaecati quod ullam at\nvoluptatem error expedita pariatur\nnihil sint nostrum voluptatem reiciendis et"
            },
            {
                "postId": 1,
                "id": 3,
                "name": "odio adipisci rerum aut animi",
                "email": "Nikita@garfield.biz",
                "body": "quia molestiae reprehenderit quasi aspernatur\naut expedita occaecati aliquam eveniet laudantium\nomnis quibusdam delectus saepe quia accusamus maiores nam est\ncum et ducimus et vero voluptates excepturi deleniti ratione"
            }]

    # Test długości listy postów
    @patch('requests.get')
    def test_posts_length(self, mock_get):
        mock_get.return_value.json.return_value = self.fake_posts
        posts = repository.get_posts()
        self.assertNotEqual(len(posts), 0)

    # Test długości listy albumów
    @patch('requests.get')
    def test_albums_length(self, mock_get):
        mock_get.return_value.json.return_value = self.fake_albums
        albums = repository.get_albums()
        self.assertNotEqual(len(albums), 0)

    # Test istnienia postu
    @patch('requests.get')
    def test_post_exists(self, mock_get):
        mock_get.return_value.json.return_value = self.fake_posts[1]
        post = repository.get_post(1)
        self.assertNotEqual(len(post), 0)

    # Test struktury postu
    @patch('requests.get')
    def test_post_structure(self, mock_get):
        mock_responses = [
            self.fake_posts[1],  # post
            self.fake_users[1],  # user
            self.fake_comments  # comments
        ]

        mock_get.side_effect = [MagicMock(json=MagicMock(return_value=response)) for response in mock_responses]

        post = repository.get_post(1)

        self.assertIn("post", post)
        self.assertIn("id", post["post"])
        self.assertIn("userId",  post["post"])
        self.assertIn("title",  post["post"])
        self.assertIn("body",  post["post"])

        self.assertIn("user", post)
        self.assertIn("id", post["user"])
        self.assertIn("name", post["user"])

        self.assertIn("comments", post)
        self.assertNotEqual(len(post["comments"]), 0)

    # Test złego ID postu
    @patch('requests.get')
    def test_post_with_wrong_id(self, mock_get):
        mock_get.return_value.json.return_value = {}
        post = repository.get_post("No photos found")
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
        mock_get.return_value.json.return_value =  self.fake_photos
        photos = repository.get_photos(1)
        self.assertNotEqual(len(photos), 0)

    # # Test złego ID zdjęć
    # @patch('requests.get')
    # def test_photos_with_wrong_id(self, mock_get):
    #     mock_get.return_value.json.return_value = [] 
    #     photo = repository.get_photos("niepoprawny argument")
    #     # self.assertEqual(len(photo), 0)
    #     self.assertEqual(response.status_code, 404)

    # # Test pobierania zdjęć dla niestniejącego albumu
    # @patch('requests.get')
    # def test_photos_with_not_existing_id(self, mock_get):
    #     mock_get.return_value.json.return_value = []  
    #     photo = repository.get_photos(-1)
    #     self.assertEqual(len(photo), 0)

    # Test istnienia zdjęć
    @patch('requests.get')
    def test_get_photos_non_empty(self, mock_get):
        mock_get.return_value.json.return_value = self.fake_photos
        photos = repository.get_photos(1)
        self.assertTrue(all(len(photo) > 0 for photo in photos))

    # Test istnienia kluczy w postach
    @patch('requests.get')
    def test_get_post_keys(self, mock_get):
        mock_get.return_value.json.return_value = self.fake_posts[1]
        post = repository.get_post(1)
        self.assertIn("post", post)
        self.assertIn("user", post)
        self.assertIn("comments", post)

    # Test typu postu
    @patch('requests.get')
    def test_get_post_type(self, mock_get):
        mock_get.return_value.json.return_value = self.fake_posts[1]
        post = repository.get_post(1)
        self.assertIsInstance(post, dict)

    # Test typu albumu
    @patch('requests.get')
    def test_get_albums_type(self, mock_get):
        mock_get.return_value.json.return_value = self.fake_albums
        albums = repository.get_albums()
        self.assertIsInstance(albums, list)

    # Test typu zdjęć
    @patch('requests.get')
    def test_get_photos_type(self, mock_get):
        mock_get.return_value.json.return_value = self.fake_photos
        photos = repository.get_photos(1)
        self.assertIsInstance(photos, list)

    # Test istnienia klucza usera
    @patch('requests.get')
    def test_get_post_user_keys(self, mock_get):
        mock_get.return_value.json.return_value = self.fake_posts[1]
        post = repository.get_post(1)
        self.assertIn("id", post["user"])

    # Test istnienia klucza w zdjęciach
    @patch('requests.get')
    def test_get_photos_keys(self, mock_get):
        mock_get.return_value.json.return_value = self.fake_photos
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
            self.fake_posts[1],  # post
            self.fake_users[1],  # user
            self.fake_comments  # comments
        ]

        mock_get.side_effect = [MagicMock(json=MagicMock(return_value=response)) for response in mock_responses]

        post = repository.get_post(1)

        for comment in post["comments"]:
            self.assertIn("id", comment)
            self.assertIn("name", comment)
            self.assertIn("email", comment)

if __name__ == '__main__':
    unittest.main()
