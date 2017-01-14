#!/usr/bin/env python3

import json
import urllib.error
import urllib.parse
import urllib.request


req = urllib.request.Request(
    "https://httpbin.org:443/get?%s" % urllib.parse.urlencode({'show_env': '1'})
)

print("---url-----------------------------")
print(req.full_url)

print("---HTTP METHOD---------------------")
print(req.get_method())

try:
    rsp = urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print(e)
    exit(1)

rspHeader = rsp.info()
rspContent = rsp.read()

rsp.close()

print("---url-----------------------------")
print(rsp.url)

print("---status code---------------------")
print(rsp.getcode())

print("---response header-----------------")
print(rspHeader.items())

print("---response content encoding-------")
print(rspHeader.get_content_charset())

print("---binary response content---------")
print(rspContent)

print("---response content----------------")
print(rspContent.decode('utf-8'))

print("---json format response content----")
print(json.loads(rspContent.decode('utf-8')))
