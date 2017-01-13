#!/usr/bin/env python3

import json
import ssl

from http.server import BaseHTTPRequestHandler, HTTPServer


class MyHttpHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print("PATH: " + self.path)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        msg = json.dumps(
            {'4': 5, '6': 7},
            sort_keys=True,
            indent=4,
            separators=(',', ': ')
        )

        self.wfile.write(bytes(msg, "utf-8"))

httpd = HTTPServer(('127.0.0.1', 8000), MyHttpHandler)

httpd.socket = ssl.wrap_socket(
    httpd.socket,
    certfile='./server.pem',
    server_side=True
)

httpd.serve_forever()