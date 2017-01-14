#!/usr/bin/env python3

import flask


app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def my_root_handler():
    print("PATH: " + flask.request.query_string.decode("utf-8"))

    return flask.make_response(
        flask.jsonify(
            {'id': 'xxx-xxxx', 'content': 'TBD'}
        ),
        200
    )

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=8000
    )
