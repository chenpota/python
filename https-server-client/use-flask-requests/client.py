#!/usr/bin/env python3

import requests


requests.packages.urllib3.disable_warnings(
    requests.packages.urllib3.exceptions.SubjectAltNameWarning
)

try:
    rsp = requests.get(url='https://127.0.0.1:8000', verify='server.pem')
except requests.exceptions.ConnectionError as e:
    print(e)
    exit(1)

print("---url-----------------------------")
print(rsp.url)

print("---status code---------------------")
print(rsp.status_code)

print("---response header-----------------")
print(rsp.headers)

print("---binary response content---------")
print(rsp.content)
