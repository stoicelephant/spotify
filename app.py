from flask import Flask, request, url_for, session, redirect
import spotipy 
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)
app.secret_key = 'temp_secret_key'
app.config['SESSION_COOKIE_NAME'] = 'spotify-login-session'
TOKEN_INFO = 'token_info'


@app.route('/')
def login():
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/redirect')
def redirectPage():
    sp_oauth = create_spotify_oauth()
    session.clear()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    session[TOKEN_INFO] = token_info
    return redirect(url_for('getStickers',_external=True))
 
@app.route('/getStickers')
def getStickers():
    try:
        token_info = get_token()
    except:
        print()
    token_info = get_token()
    return 'Page to retrieve stickers'

def get_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        raise "exception"

def create_spotify_oauth():
    return SpotifyOAuth(
            client_id= '26af341e509a46c38ae343c5a1f07fc4',
            client_secret = '6a43fb3bf52a4fbfb4f6600e47ba6259',
            redirect_uri = url_for('redirectPage',_external=True),
            scope = 'user-library-read')