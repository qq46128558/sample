#!/usr/bin/env python3

'马蜂窝城市旅游数据分析'

import logging
from urllib.request import urlopen
import urllib.request as request
from bs4 import BeautifulSoup


def get_one_page(url):
	headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
	myrequest=request.Request(url,headers=headers)
	logging.info(myrequest)
	# INFO:root:<urllib.request.Request object at 0x0000020633C26CF8>
	html=urlopen(myrequest)
	logging.info(type(html.read()))
	# INFO:root:<class 'bytes'>
	return html.read()



def get_cat_url(html):
	soup=BeautifulSoup(html,'html.parser')
	pass

if __name__=='__main__':
	logging.basicConfig(level=logging.INFO)
	baseurl="http://www.mafengwo.cn/mdd/"
	html=get_one_page(baseurl)
	get_cat_url(html)
