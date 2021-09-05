""" 
Middleman app Python_Flask_Finance
Will be incorporating Plaid to see investments and bank accounts all in one spot
"""
import os

import flask_login
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'super secret string'  # Change this!

login_manager = LoginManager()
login_manager.init_app(app)

# Our mock database.
users = {'admin': {'password': 'pass'}}


class User(flask_login.UserMixin):
    """Temp User class for starting to tackle login functionality, will move this out later"""
    pass


@login_manager.user_loader
def user_loader(email):
    """Login Management, checks that user exists"""
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    """Login Management, checks that user exists"""
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['password'] == users[email]['password']

    return user


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Serves Login Form and redirects."""
    if request.method == 'GET':
        return render_template("login.html")

    email = request.form['email']
    if request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return redirect(url_for('test'))

    return 'Bad login'


@app.route("/")
def home():
    """Serves Home Page."""
    return render_template("index.html")


@app.route("/test", methods=['GET', 'POST'])
@flask_login.login_required
def test():
    """Serves Test Page."""
    return render_template("test.html")


@app.route('/favicon.ico')
def favicon():
    """Serves favicon."""
    return send_from_directory(os.path.join(app.root_path, 'static', 'images'),
                               'favicon.ico', mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=True)
