from flask import Flask, render_template
import requests

app = Flask(__name__)

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