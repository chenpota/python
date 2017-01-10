#!/usr/bin/env python3

import json
import socket
import http.client

conn = http.client.HTTPSConnection('httpbin.org')

try:
    conn.request('GET', '/get?show_env=1')
except socket.gaierror as e:
    print(e)
    exit(1)

httpRsp = conn.getresponse()
rspContent = httpRsp.read()
httpMsg = httpRsp.msg

conn.close()

print("---status code---------------------")
print(httpRsp.status)

print("---response header-----------------")
print(httpRsp.getheaders())
print(httpMsg.items())

print("---binary response content---------")
print(rspContent)

print("---response content encoding-------")
print(httpMsg.get_content_charset())

print("---response content----------------")
print(rspContent.decode('utf-8'))

print("---json format response content----")
print(json.loads(rspContent.decode('utf-8')))
