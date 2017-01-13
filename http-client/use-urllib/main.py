#!/usr/bin/env python3

import json
import ssl

from urllib.error import HTTPError
from urllib.request import Request, urlopen
from urllib.parse import urlencode

req = Request("https://httpbin.org/get?%s" % urlencode({'show_env': '1'}))

print("---url-----------------------------")
print(req.get_full_url())

print("---HTTP METHOD---------------------")
print(req.get_method())

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_REQUIRED

try:
    rsp = urlopen(req, context=ctx)
except HTTPError as e:
    print(e)
    exit(1)

httpMsg = rsp.info()
rspContent = rsp.read()

print("---url-----------------------------")
print(rsp.url)

print("---status code---------------------")
print(rsp.getcode())

print("---response header-----------------")
print(httpMsg.items())

print("---binary response content---------")
print(rspContent)

print("---response content encoding-------")
print(httpMsg.get_content_charset())

print("---response content----------------")
print(rspContent.decode('utf-8'))

print("---json format response content----")
print(json.loads(rspContent.decode('utf-8')))
