import requests
from flask import abort
import logging

def get_posts():
    # Get posts from the API
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        posts = response.json()
        return posts
    except Exception as e:
        abort(500, description="Error: %s" % e)
        logging.error(f'Error: {e}')

def get_post(post_id):
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/posts/%s'%(post_id))
        post = response.json()
        if len(post)>0:
            response = requests.get('https://jsonplaceholder.typicode.com/users/%s' % (post["userId"]))
            user=response.json()
            response = requests.get('https://jsonplaceholder.typicode.com/comments?postId=%s' %(post_id))
            comments=response.json()
            return {"post": post, "user": user, "comments": comments}
        else:
            return {}
    except Exception as e:
        abort(500, description="Error: %s" % e)
        logging.error(f'Error: {e}')


def get_albums():
    response = requests.get('https://jsonplaceholder.typicode.com/albums')
    albums = response.json()
    if not albums:
        abort(404, description="No album found")
        logging.error(f'No album found')
    else:
        return albums        
    
def get_photos(album_id):
    response = requests.get('https://jsonplaceholder.typicode.com/photos?albumId=%s' %(album_id))
    photos = response.json()
    if not photos:
        abort(404, description="No photos found")
        logging.error(f'No photos found')
    else:
        return photos