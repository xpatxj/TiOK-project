from flask import Flask, Blueprint, render_template, g, abort
import requests
import logging
import repository

albums_bp = Blueprint('albums', __name__, url_prefix='/albums')

@albums_bp.route('/')
def albums():
    try:
      g.albums = repository.get_albums()
      if not g.albums:
          abort(404, description="No albums found")
      else:
        g.rows = len(g.albums)//4
        g.columns = len(g.albums)%4
        if g.columns>0:
          g.rows+=1

        return render_template('albums.html')
    except Exception as e:
        logging.error(f'Error: {e}')
        abort(404, description="Error: %s" % e)

@albums_bp.route('/<album_id>/photos')
def photos(album_id):
    try:
        g.photos = repository.get_photos(album_id)
        if not g.photos:
            abort(404, description="No photos found")
        else:
          return render_template('photos.html')
    except Exception as e:
        abort(404, description="Error: %s" % e)
        logging.error(f'Error: {e}')