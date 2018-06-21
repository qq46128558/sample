#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# token = "<your api key>"
# webRequest = urllib.request.Request("http://myapi.com", headers={"token":token})
# html = urlopen(webRequest)

'使用python调用商派BBC API接口示例'

from urllib.request import Request
from urllib.request import urlopen

from datetime import datetime
import hashlib
import requests
import json
import urllib

def assemble(data={}):
    # dictionary数据类型是无序的 (dictionary keys 排序方法)
    items=[(k,data[k]) for k in sorted(data.keys())] 
    sign=""
    for t in items:
        if (t[1]==None):
            continue
        if (type(t[1])==bool):
            t[1]='1' if t[1] else '0'
        sign+=t[0]+str(t[1])
    return sign

data={
    "method":"trade.get.list",
    "timestamp": int(datetime.now().timestamp()),
    "format":"json",
    "v":"v1",
    "sign_type":"MD5",
    "fields":"*",
}
token=''
# 有中文值时报错(未解决): UnicodeEncodeError: 'latin-1' codec can't encode characters in position 0-1: ordinal not in range(256)

# data["sign"]=hashlib.md5((hashlib.md5(assemble(data).encode('utf-8')).hexdigest().upper()+token).encode('utf-8')).hexdigest().upper()
sign=assemble(data)
# MD5加密
sign=hashlib.md5(sign.encode('utf-8')).hexdigest()
# 转大写
sign=sign.upper()+token
sign=sign.encode('utf-8')
sign=hashlib.md5(sign).hexdigest().upper()
data["sign"]=sign
# print(sign)

url="http://192.168.239.138/index.php/api"

# 方法一(urllib.request.Request)
data=urllib.parse.urlencode(data).encode(encoding='UTF8')
webRequest=Request(url,data=data,method="POST")
html=urlopen(webRequest)
print(html.read())

# 方法二(requests) (自动解码unicode)
# html=requests.post(url,data=data)
# print(html.json())