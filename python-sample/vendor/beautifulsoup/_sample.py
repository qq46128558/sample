#!/usr/bin/env python3

'Beautiful Soup 4.2.0 用法示例'

import logging
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup=BeautifulSoup(html_doc,"html.parser")

# 按照标准的缩进格式的结构输出
logging.info(soup.prettify())

# 浏览结构化数据
logging.info(soup.title)
# INFO:root:<title>The Dormouse's story</title>
logging.info(soup.title.name)
# INFO:root:title
