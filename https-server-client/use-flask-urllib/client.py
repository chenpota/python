#!/usr/bin/env python3

import json
import ssl
import urllib.error
import urllib.parse
import urllib.request


req = urllib.request.Request("https://127.0.0.1:8000/")

ctx = ssl.create_default_context(cafile='server.pem')
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_REQUIRED

try:
    rsp = urllib.request.urlopen(req, context=ctx)
except urllib.error.HTTPError as e:
    print(e)
    exit(1)

print("---status code---------------------")
print(rsp.getcode())

print("---response header-----------------")
print(rsp.info())

print("---binary response content---------")
print(rsp.read())

rsp.close()
