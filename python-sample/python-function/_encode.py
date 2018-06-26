#!/usr/bin/env python

""" python3各种编码解码记录 """

__author__='peter'

from urllib import parse


# 获取url参数
url=r'https://docs.python.org/3.5/search.html?q=parse&check_keywords=yes&area=default'
params=parse.urlparse(url)
print(params)
# ParseResult(scheme='https', netloc='docs.python.org', path='/3.5/search.html', params='', query='q=parse&check_keywords=yes&area=default', fragment='')
print(params.scheme)
# https
print(params.query)
# q=parse&check_keywords=yes&area=default
print(parse.parse_qs(params.query))
# {'q': ['parse'], 'check_keywords': ['yes'], 'area': ['default']}

# urlencode 拼接url参数
print(parse.urlencode({'key1':'abc','key2':123}))
# key1=abc&key2=123

# quote/quote_plus (urlencode编码)
print(parse.quote('珠海/深圳'))
# %E7%8F%A0%E6%B5%B7/%E6%B7%B1%E5%9C%B3
print(parse.quote_plus('珠海/深圳'))
# %E7%8F%A0%E6%B5%B7%2F%E6%B7%B1%E5%9C%B3

# unquote/unquote_plus (urlencode解码)
print(parse.unquote('%E7%8F%A0%E6%B5%B7'))
# 珠海
