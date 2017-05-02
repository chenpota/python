#!/usr/bin/env python3

import logging

from socketIO_client import BaseNamespace
from socketIO_client import SocketIO


class MyNamespace(BaseNamespace):

    def on_connect(self):
        print("on_connect.")

    def on_reconnect(self):
        print("on_reconnect.")

    def on_disconnect(self):
        print("on_disconnect.")

    def on_event(self, event, *args):
        print("on_event.")

    def on_error(self, data):
        print("on_error.")

    def on_msg_from_server(self, data):
        print("on_msg_from_server:", data)
        self.emit('msg_from_client', "Hello, server!")


logging.getLogger('socketIO-client').setLevel(logging.DEBUG)
logging.basicConfig()

sio = SocketIO('127.0.0.1', 12345, MyNamespace)
myns = sio.define(MyNamespace, '/my_namespace')

sio.wait(seconds=1)
