#!/usr/bin/env python3

import requests
from requests.auth import HTTPDigestAuth

# example 1
rsp = requests.get('http://localhost:5000',
                   auth=HTTPDigestAuth('username', 'password'))

print(rsp.status_code)
print(rsp.text)

# example 2
session = requests.Session()
session.auth = HTTPDigestAuth('username', 'password')

rsp = session.get('http://localhost:5000')

print(rsp.status_code)
print(rsp.text)
