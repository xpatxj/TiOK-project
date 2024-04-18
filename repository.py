import requests
from flask import abort
def get_posts():
    # Get posts from the API
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = response.json()
    return posts

def get_post(post_id):
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

def get_albums():
    response = requests.get('https://jsonplaceholder.typicode.com/albums')
    albums = response.json()
    if not albums:
        abort(404, description="No album found")
    else:
        return albums
    
def get_photos(album_id):
    response = requests.get('https://jsonplaceholder.typicode.com/photos?albumId=%s' %(album_id))
    photos = response.json()
    if not photos:
        abort(404, description="No photos found")
    else:
        return photos