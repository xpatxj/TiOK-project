import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import repository

class TestRepository(unittest.TestCase):

    def test_posts_length(self):
        posts = repository.get_posts()
        self.assertEqual(len(posts), 100)

    def test_albums_length(self):
        albums = repository.get_albums()
        self.assertEqual(len(albums), 100)

    def test_post_exists(self):
        post = repository.get_post(1)
        self.assertNotEqual(len(post), 0)

    def test_post_structure(self):
        post = repository.get_post(1)
        self.assertNotEqual(len(post["user"]), 0)
        self.assertNotEqual(len(post["comments"]), 0)

    def test_post_with_wrong_id(self):
        post = repository.get_post("niepoprawny argument")
        self.assertEqual(len(post), 0)

    def test_post_with_not_existing_id(self):
        post = repository.get_post(-1)
        self.assertEqual(len(post), 0)

    def test_photos_length(self):
        photos = repository.get_photos(1)
        self.assertNotEqual(len(photos), 0)

    def test_photos_with_wrong_id(self):
        photo = repository.get_photos("niepoprawny argument")
        self.assertEqual(len(photo), 0)

    def test_photos_with_not_existing_id(self):
        photo = repository.get_photos(-1)
        self.assertEqual(len(photo), 0)

    def test_get_photos_non_empty(self):
        photos = repository.get_photos(1)
        self.assertTrue(all(len(photo) > 0 for photo in photos))

    def test_get_post_keys(self):
        post = repository.get_post(1)
        self.assertIn("post", post)
        self.assertIn("user", post)
        self.assertIn("comments", post)

if __name__ == '__main__':
    unittest.main()
