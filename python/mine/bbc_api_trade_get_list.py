#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# token = "<your api key>"
# webRequest = urllib.request.Request("http://myapi.com", headers={"token":token})
# html = urlopen(webRequest)

'使用python调用商派BBC API接口示例'

from urllib.request import Request
from urllib.request import urlopen
from datetime import datetime


headers={
    "method":"trade.get.list",
    "timestamp":int(datetime.now().timestamp()),
    "format":"json",
    "v":"v1",
    "sign_type":"MD5",
    "fields":"*",
}
token=''
# UnicodeEncodeError: 'latin-1' codec can't encode characters in position 0-1: ordinal not in range(256) 中文错误?
headers["sign"]="利用token计算签名"

webRequest=Request("http://192.168.239.138/index.php/api",headers=headers)
html=urlopen(webRequest)
print(html.read())