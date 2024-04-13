from flask import Flask, Blueprint, render_template, g
import requests
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
  return requests.get('https://jsonplaceholder.typicode.com/albums').json()

def fake_photos_get(count):
  return requests.get('https://jsonplaceholder.typicode.com/photos').json()