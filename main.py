from flask import Flask, render_template, g, abort
from albums import albums_bp
import repository
import requests
import logging

# #przygotowanie loggera
logger = logging.getLogger(__name__)
logging.basicConfig(filename='TiOK.log', encoding='utf-8', level=logging.DEBUG, format='%(process)s : %(levelname)s : %(asctime)s %(message)s', datefmt='%d-%b-%y %H:%M:%S')

# Tworzenie wiadomości logów
logging.debug('Omg super zdebugowało się!')
logging.info('Aplikacja wystartowała')
logging.warning('To jest achtung.')
logging.error('ERROR! ERROR! ERROR!')
logging.critical('CRIIITICAL! CRIIITICAL! CRIIITICAL!')

app = Flask(__name__)
app.register_blueprint(albums_bp)

@app.route('/')
def home():
    try:
        return render_template('index.html', posts=repository.get_posts())
    except Exception as e:
        logging.error(f'Error: {e}')
        return 'Error'

@app.route('/post/<post_id>')
def post(post_id):
    try:
        post = repository.get_post(post_id)
        if not post:
            abort(404, description="Post not found")
        else:
            if len(post)>0:
                return render_template('post.html', post=post["post"], user=post["user"], comments=post["comments"])
            else:
                return home()
    except Exception as e:
        logging.error(f'Error: {e}')
        abort(404, description="Error: %s" % e)

if __name__ == '__main__':
    app.run(debug=True)