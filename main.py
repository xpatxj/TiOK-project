from flask import Flask, render_template, g
from albums import albums_bp
import requests

app = Flask(__name__)
app.register_blueprint(albums_bp)


@app.route('/')
def home():

    # Get posts from the API
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = response.json()

    return render_template('index.html', posts=posts)

@app.route('/albums')
def albums():
    return render_template('albums.html')

if __name__ == '__main__':
    app.run(debug=True)