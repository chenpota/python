#!/usr/bin/env python3

import http.client
import json
import socket


conn = http.client.HTTPSConnection(host='httpbin.org', port=443)

try:
    conn.request('GET', '/get?show_env=1')
except socket.gaierror as e:
    print(e)
    exit(1)

httpRsp = conn.getresponse()
rspHeader = httpRsp.msg
rspContent = httpRsp.read()

conn.close()

print("---status code---------------------")
print(httpRsp.status)

print("---response header-----------------")
print(httpRsp.getheaders())
print(rspHeader.items())

print("---response content encoding-------")
print(rspHeader.get_content_charset())

print("---binary response content---------")
print(rspContent)

print("---response content----------------")
print(rspContent.decode('utf-8'))

print("---json format response content----")
print(json.loads(rspContent.decode('utf-8')))
