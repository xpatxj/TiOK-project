from flask import Flask, render_template, g
from albums import albums_bp
import repository
import requests
import logging

#przygotowanie loggera
logger = logging.getLogger(__name__)
logging.basicConfig(filename='c:\\temp\\TiOK.log', encoding='utf-8', level=logging.DEBUG, format='%(levelname)s:%(asctime)s %(message)s', datefmt='%T')

app = Flask(__name__)
app.register_blueprint(albums_bp)


@app.route('/')
def home():
    return render_template('index.html', posts=repository.get_posts())

@app.route('/post/<post_id>')
def post(post_id):
    post = repository.get_post(post_id)

    if len(post)>0:
        return render_template('post.html', post=post["post"], user=post["user"], comments=post["comments"])
    else:
        return home()

if __name__ == '__main__':
    app.run(debug=True)