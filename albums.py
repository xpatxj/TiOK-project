from flask import Flask, Blueprint, render_template, g
import logging

albums_bp = Blueprint('albums', __name__, url_prefix='/albums')

@albums_bp.route('/')
def albums():
    g.albums = fake_albums_get(10)
    g.rows = len(g.albums)//4
    g.columns = len(g.albums)%4
    if g.columns>0:
      g.rows+=1

    return render_template('albums.html')

@albums_bp.route('/<album_id>/photos')
def photos(album_id):
    g.photos =fake_photos_get(10)
    return render_template('photos.html')


def fake_albums_get(count):
  return [{
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

def fake_photos_get(count):
    return [
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