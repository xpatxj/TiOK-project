from flask import Flask, Blueprint, render_template, g
import requests
import logging

import repository

albums_bp = Blueprint('albums', __name__, url_prefix='/albums')

@albums_bp.route('/')
def albums():
    g.albums = repository.get_albums()
    g.rows = len(g.albums)//4
    g.columns = len(g.albums)%4
    if g.columns>0:
      g.rows+=1

    return render_template('albums.html')

@albums_bp.route('/<album_id>/photos')
def photos(album_id):
    g.photos =repository.get_photos(album_id)
    return render_template('photos.html')
