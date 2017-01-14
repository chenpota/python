#!/usr/bin/env python3

import requests


try:
    r = requests.get(url='http://httpbin.org:80/get',
                     params={'show_env': '1'})
except requests.exceptions.ConnectionError as e:
    print(e)
    exit(1)

print("---url-----------------------------")
print(r.url)

print("---status code---------------------")
print(r.status_code)

print("---response header-----------------")
print(r.headers)

print("---response content encoding-------")
print(r.encoding)

print("---binary response content---------")
print(r.content)

print("---response content----------------")
print(r.text)

print("---json format response content----")
print(r.json())
