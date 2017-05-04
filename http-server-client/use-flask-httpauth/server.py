#!/usr/bin/env python3

from flask import Flask
from flask import g
from flask_httpauth import HTTPBasicAuth
from flask_httpauth import HTTPDigestAuth
from flask_httpauth import MultiAuth
from werkzeug.security import generate_password_hash, check_password_hash

APP = Flask(__name__)
APP.config['SECRET_KEY'] = 'secret'

BASIC_AUTH = HTTPBasicAuth()
DIGEST_AUTH = HTTPDigestAuth()
MULTI_AUTH = MultiAuth(DIGEST_AUTH, BASIC_AUTH)


@BASIC_AUTH.verify_password
def verify_password(username, password):
    g.user = username
    return username == 'username' and check_password_hash(generate_password_hash('password'), password)


@DIGEST_AUTH.get_password
def get_pw(username):
    if username == 'username':
        g.user = username
        return 'password'

    return None


@APP.route('/')
@MULTI_AUTH.login_required
def index():
    return 'Hello, {0}!'.format(g.user)


if __name__ == '__main__':
    APP.run()
