#!/usr/bin/env python3

import requests

r = requests.get('http://httpbin.org/get', params={'show_env': '1'})

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
