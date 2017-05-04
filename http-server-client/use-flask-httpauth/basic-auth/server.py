#!/usr/bin/env python3

from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

APP = Flask(__name__)
APP.config['SECRET_KEY'] = 'secret'
AUTH = HTTPBasicAuth()


@AUTH.verify_password
def verify_password(username, password):
    return username == 'username' and check_password_hash(generate_password_hash('password'), password)


@APP.route('/')
@AUTH.login_required
def index():
    return 'Hello, {0}!'.format(AUTH.username())


if __name__ == '__main__':
    APP.run()
