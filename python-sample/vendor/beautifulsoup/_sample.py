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
<b><!--Hey, buddy. Want to buy a used parser?--></b>
"""
# html.parser lxml ["lxml", "xml"] xml html5lib
soup=BeautifulSoup(html_doc,"html.parser")

# 按照标准的缩进格式的结构输出
logging.info(soup.prettify())

'''几个浏览结构化数据的方法'''
logging.info(soup.title)
# INFO:root:<title>The Dormouse's story</title>

logging.info(soup.title.name)
# INFO:root:title

logging.info(soup.title.string)
logging.info(soup.title.text)
logging.info(soup.title.get_text())
# INFO:root:The Dormouse's story

logging.info(soup.title.parent.name)
# INFO:root:head

logging.info(soup.p['class'])
logging.info(soup.p.get('class'))
# INFO:root:['title']

logging.info(soup.find_all('a'))
# INFO:root:[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

logging.info(soup.find(id="link3"))
# INFO:root:<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>


'''从文档中找到所有<a>标签的链接:'''
for link in soup.find_all('a'):
	logging.info(link.get('href'))
# INFO:root:http://example.com/elsie
# INFO:root:http://example.com/lacie
# INFO:root:http://example.com/tillie


# Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种: Tag , NavigableString , BeautifulSoup , Comment .

'''Tag'''
# Tag 对象与XML或HTML原生文档中的tag相同:
# tag的属性操作方法与字典一样
tag=soup.a
logging.info(type(tag))
# INFO:root:<class 'bs4.element.Tag'>
logging.info(tag.attrs)
# INFO:root:{'href': 'http://example.com/elsie', 'class': ['sister'], 'id': 'link1'}
# 删除属性
del tag['class']
logging.info(soup.a)
# INFO:root:<a href="http://example.com/elsie" id="link1">Elsie</a>
tag['class']=['sister']


'''NavigableString '''
# 字符串常被包含在tag内.Beautiful Soup用 NavigableString 类来包装tag中的字符串
logging.info(tag.string)
# INFO:root:Elsie
logging.info(type(tag.string))
# INFO:root:<class 'bs4.element.NavigableString'>
tag.string='Peter'
tag.string.replace_with("Peter")
logging.info(tag)
# INFO:root:<a class="sister" href="http://example.com/elsie" id="link1">Peter</a>


'''BeautifulSoup'''
# BeautifulSoup 对象表示的是一个文档的全部内容.大部分时候,可以把它当作 Tag 对象,它支持 遍历文档树 和 搜索文档树 中描述的大部分的方法
logging.info(soup.name)
# INFO:root:[document]


'''Comment'''
# Tag , NavigableString , BeautifulSoup 几乎覆盖了html和xml中的所有内容,但是还有一些特殊对象.容易让人担心的内容是文档的注释部分
comment=soup.find_all('b')[1].string
logging.info(comment)
# INFO:root:Hey, buddy. Want to buy a used parser?
logging.info(type(comment))
# INFO:root:<class 'bs4.element.Comment'>

'''遍历文档树'''
# 将tag的子节点以列表的方式输出
# 由于上面的文字有换行, 所以这里0是换行,1才是html
logging.info(soup.contents[1].name)
# INFO:root:html
logging.info(soup.body.p.contents)
# INFO:root:[<b>The Dormouse's story</b>]
logging.info(soup.body.contents[-2])
# INFO:root:<b><!--Hey, buddy. Want to buy a used parser?--></b>

# 对tag的子节点进行循环(一级子节点)
for child in soup.body.children:
	if child.name=='b':
		logging.info(child.string)
# INFO:root:Hey, buddy. Want to buy a used parser?

'''.contents 和 .children 属性仅包含tag的直接子节点'''
# 对所有tag的子孙节点进行递归循环
for child in soup.body.descendants:
	if child.name=='b':
		logging.info(child.string)
# INFO:root:The Dormouse's story
# INFO:root:Hey, buddy. Want to buy a used parser?

# 如果tag中包含多个字符串 [2] ,可以使用 .strings 来循环获取
# 输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容:
for string in soup.stripped_strings:
	logging.debug(string)

# 父节点
logging.info(soup.title.string.parent)
# INFO:root:<title>The Dormouse's story</title>

# 遍历所有父节点
for parent in soup.a.parents:
	logging.info(parent.name)
# INFO:root:p
# INFO:root:body
# INFO:root:html
# INFO:root:[document]
