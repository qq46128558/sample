#! /usr/bin/env python3

""" HTTP 认证 """

import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

auth=HTTPBasicAuth('Ryan','password')
r=requests.post(url="http://pythonscraping.com/pages/auth/login.php",auth=auth)
print(r.text)
