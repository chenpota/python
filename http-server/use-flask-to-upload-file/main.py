#!/usr/bin/env python3

import os
from flask import Flask, redirect, render_template, request
from werkzeug.utils import secure_filename


APP = Flask(__name__)
APP.config['MAX_CONTENT_LENGTH'] = 1024


@APP.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        return render_template('choose_file.html')

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    file.save(os.path.join('./', file.filename))
    return "Upload {0} successfully".format(file.filename), 200


if __name__ == '__main__':
    APP.run(
        host='127.0.0.1',
        port=8000
    )
