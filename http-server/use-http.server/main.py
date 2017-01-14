#!/usr/bin/env python3

import http.server
import json


class MyHttpHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("PATH: " + self.path)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        msg = json.dumps(
            {'id': 'xxx-xxxx', 'content': 'TBD'},
            indent=4,
            separators=(',', ': ')
        )

        self.wfile.write(bytes(msg, "utf-8"))

httpd = http.server.HTTPServer(('127.0.0.1', 8000), MyHttpHandler)

httpd.serve_forever()
