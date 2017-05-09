#!/usr/bin/env python3

import os
from flask import Flask, redirect, render_template, request, send_from_directory


APP = Flask(__name__)


@APP.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@APP.route('/redirect', methods=['GET'])
def redirect_url():
    return redirect(request.url_root + 'download/test.file')


@APP.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory('./download', filename)


if __name__ == '__main__':
    APP.run(
        host='127.0.0.1',
        port=8000
    )
