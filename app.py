from flask import Flask, redirect, url_for, session, request
from requests_oauthlib import OAuth2Session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# OAuth 2.0 Client Information
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
authorization_base_url = 'https://accounts.google.com/o/oauth2/auth'
token_url = 'https://accounts.google.com/o/oauth2/token'
scope = ['openid', 'email', 'profile']
redirect_uri = 'http://localhost:5000/callback'

# Step 1: User Authorization.
@app.route('/login')
def login():
    google = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)
    authorization_url, state = google.authorization_url(authorization_base_url, access_type="offline", prompt="select_account")
    
    # State is used to prevent CSRF, keep this for later.
    session['oauth_state'] = state
    return redirect(authorization_url)

# Step 2: User authorized the client, get the token.
@app.route('/callback')
def callback():
    google = OAuth2Session(client_id, state=session['oauth_state'], redirect_uri=redirect_uri)
    token = google.fetch_token(token_url, client_secret=client_secret, authorization_response=request.url)
    
    # Save the token in session for later use.
    session['oauth_token'] = token
    
    return redirect(url_for('.profile'))

@app.route('/profile')
def profile():
    google = OAuth2Session(client_id, token=session['oauth_token'])
    response = google.get('https://www.googleapis.com/oauth2/v1/userinfo')
    
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)
