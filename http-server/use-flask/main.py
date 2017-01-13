#!/usr/bin/env python3

from flask import Flask, jsonify, make_response, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def my_get_handler():
    print("PATH: " + request.query_string.decode("utf-8"))

    return make_response(
        jsonify(
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
        threaded=True,
        debug=True,
        ssl_context=('server.pem', 'server.key')
    )
