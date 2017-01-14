#!/usr/bin/env python3

import flask


app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def my_get_handler():
    return flask.make_response(
        flask.jsonify(
            {
                'id': 'XXX-XXXX',
                'content': 'TBD'
            }
        ),
        200
    )

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=8000,
        ssl_context=('server.pem', 'server.key')
    )
