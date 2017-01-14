#!/usr/bin/env python3

import http.client
import json
import socket
import ssl

ctx = ssl.create_default_context(cafile='server.pem')
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_REQUIRED

conn = http.client.HTTPSConnection(host='127.0.0.1', port=8000, context=ctx)

try:
    conn.request('GET', '/')
except socket.gaierror as e:
    print(e)
    exit(1)

httpRsp = conn.getresponse()

conn.close()

print("---status code---------------------")
print(httpRsp.status)

print("---response header-----------------")
print(httpRsp.getheaders())

print("---binary response content---------")
print(httpRsp.read())
