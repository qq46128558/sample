#!/usr/bin/env python3

'马蜂窝城市旅游数据分析'

import logging
from urllib.request import urlopen
import urllib.request as request
from bs4 import BeautifulSoup
import re
import bs4

def get_one_page(url):
	headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
	myrequest=request.Request(url,headers=headers)
	logging.info(myrequest)
	# INFO:root:<urllib.request.Request object at 0x0000020633C26CF8>
	html=urlopen(myrequest)
	# read()一次后html就不能再read()
	html=html.read()
	logging.info(type(html))
	# INFO:root:<class 'bytes'>
	return html

# 获取大分类的url(如省)
def get_cat_url(html):
	soup=BeautifulSoup(html,'html.parser')
	# 改为正则,匹配其它大目的地 class_='hot-list clearfix'则默认为国内
	tag=soup.find_all('div',class_=re.compile('hot-list clearfix'))
	# 获取到多个hot-list DIV
	logging.debug(tag)
	# 定义一个list存放不同大目的地的大分类(如省)
	list_tag=[]

	# 循环各个DIV(大目的地)
	for i in range(0,len(tag)):
		# 查找大分类(省)
		list_tag.append(tag[i].find_all('dt'))
	logging.info("{}个大目的地:{}".format(len(list_tag),[tag.string for tag in soup.find('div',class_='r-navbar').find_all('a')]))

	# 定义list存放大分类的url
	cat_url=[]
	# 循环大目的地
	for i in range(0,len(list_tag)):
		# 循环里面的dt tag
		for tag in list_tag[i]:
			# 查找dt里面的a tag
			for a in tag.find_all('a'):
				# 找到省名及url名,写入list
				cat_url.append({"name":a.string,"url":a.attrs['href']})
	return cat_url

if __name__=='__main__':
	logging.basicConfig(level=logging.INFO)
	baseurl="http://www.mafengwo.cn/mdd/"
	html=get_one_page(baseurl)
	get_cat_url(html)
