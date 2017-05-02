#!/usr/bin/env python3

from flask import Flask
from flask_socketio import SocketIO
from flask_socketio import disconnect
from flask_socketio import emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('connect', namespace='/my_namespace')
def do_connect():
    print('do_connect')
    emit('msg_from_server', "Hello, client!", broadcast=True)


@socketio.on('msg_from_client', namespace='/my_namespace')
def do_msg_from_client(msg):
    print('do_msg_from_client:', msg)
    disconnect()


@socketio.on('disconnect', namespace='/my_namespace')
def do_disconnect():
    print('do_disconnect')


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=12345, debug=True)
