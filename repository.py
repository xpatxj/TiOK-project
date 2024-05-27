import requests
from flask import abort, Flask
import logging

cached_posts = None
cached_albums=None

def get_posts():
    global cached_posts
    # Get posts from the API
    try:
        if cached_posts is None:
            response = requests.get('https://jsonplaceholder.typicode.com/posts')
            posts = response.json()
            cached_posts = posts
        else:
            posts = cached_posts
        return posts
    except Exception as e:
        logging.error(f'Error: {e}')
        abort(500, description="Error: %s" % e)

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
        logging.error(f'Error: {e}')
        abort(500, description="Error: %s" % e)

def get_albums():
    global cached_albums
    if cached_albums is None:
        response = requests.get('https://jsonplaceholder.typicode.com/albums')
        albums = response.json()
        cached_albums = albums
    else:
        albums = cached_albums

    if not albums:
        logging.error(f'No album found')
        abort(404, description="No album found")
    else:
        return albums

def get_photos(album_id):
    response = requests.get('https://jsonplaceholder.typicode.com/photos?albumId=%s' %(album_id))
    photos = response.json()
    if not photos:
        logging.error(f'No photos found')
        abort(404, description="No photos found")
    else:
        return photos
def get_posts_range(range_left, range_right):
    # Get posts from the API
    try:
        posts=get_posts()
        filtered_posts=[]
        logging.info("Pętla")
        for post in posts:
            logging.info(f'Długość body:{len(post["body"])}')
            logging.info(f'Range left: {range_left}/{len(post["body"]) >= range_left}')
            logging.info(f'Range right: {range_right}')

            if(len(post["body"])>=range_left and len(post["body"])<=range_right):
                filtered_posts.append(post)
        return filtered_posts
    except Exception as e:
        logging.error(f'Error: {e}')
        abort(500, description="Error: %s" % e)
