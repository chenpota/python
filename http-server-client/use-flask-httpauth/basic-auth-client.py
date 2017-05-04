#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth

# example 1
rsp = requests.get('http://localhost:5000',
                   auth=HTTPBasicAuth('username', 'password'))

print(rsp.status_code)
print(rsp.text)

# example 2
session = requests.Session()
session.auth = HTTPBasicAuth('username', 'password')

rsp = session.get('http://localhost:5000')

print(rsp.status_code)
print(rsp.text)
