#!/usr/bin/env python3

import requests

from requests.exceptions import ConnectionError


#certOpt = 'mycert.crt'
certOpt = None

try:
    r = requests.get('https://httpbin.org:%s/get' % '443',
                     params={'show_env': '1'},
                     verify=certOpt)
except ConnectionError as e:
    print(e)
    exit(1)

print("---url-----------------------------")
print(r.url)

print("---status code---------------------")
print(r.status_code)

print("---response header-----------------")
print(r.headers)

print("---binary response content---------")
print(r.content)

print("---response content encoding-------")
print(r.encoding)

print("---response content----------------")
print(r.text)

print("---json format response content----")
print(r.json())
