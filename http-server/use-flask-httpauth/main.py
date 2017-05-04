#!/usr/bin/env python3

from flask import Flask
from flask_httpauth import HTTPBasicAuth

APP = Flask(__name__)
AUTH = HTTPBasicAuth()


@AUTH.get_password
def get_pw(username):
    if username == "username":
        return "password"

    return None


@APP.route('/')
@AUTH.login_required
def index():
    return "Hello, {0}!".format(AUTH.username())

if __name__ == '__main__':
    APP.run()
