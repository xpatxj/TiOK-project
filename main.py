from flask import Flask, render_template, g
from albums import albums_bp
import requests
import logging

#przygotowanie loggera
logger = logging.getLogger(__name__)
logging.basicConfig(filename='c:\\temp\\TiOK.log', encoding='utf-8', level=logging.DEBUG, format='%(levelname)s:%(asctime)s %(message)s', datefmt='%T')

app = Flask(__name__)
app.register_blueprint(albums_bp)


@app.route('/')
def home():

    # Get posts from the API
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = response.json()

    return render_template('index.html', posts=posts)

@app.route('/post/<post_id>')
def post(post_id):
    response = requests.get('https://jsonplaceholder.typicode.com/posts/%s'%(post_id))
    post = response.json()
    response = requests.get('https://jsonplaceholder.typicode.com/users/%s' % (post["userId"]))
    user=response.json()
    response = requests.get('https://jsonplaceholder.typicode.com/comments?postId=%s' %(post_id))
    comments=response.json()

    return render_template('post.html', post=post, user=user, comments=comments)


@app.route('/albums')
def albums():
    return render_template('albums.html')

if __name__ == '__main__':
    app.run(debug=True)