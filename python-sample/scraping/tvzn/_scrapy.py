#!/usr/bin/env python3

'爬取电视指南网延禧攻略信息'
'多线程|正则分割'
# http://www.tvzn.com/14784/yanyuanbiao.html

import logging
from urllib.request import urlopen
import urllib.request as request
from bs4 import BeautifulSoup
import time
import pandas as pd
import threading
import re

# 获取一个页面
def get_one_page(url):
	headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
	myrequest=request.Request(url,headers=headers)
	logging.debug(myrequest)
	html=urlopen(myrequest)
	# read()一次后html就不能再read()
	html=html.read()
	logging.debug(type(html))
	return html

# 获取演员名单
def get_actors(html):
	actor=[]
	soup=BeautifulSoup(html,'html.parser')
	tags=soup.div.find(class_='mh-pic-list').ul.find_all('li')
	for tag in tags:
		logging.debug(tag)
		actor.append({'role':tag.a.span.text,'name':tag.p.a.text,'href':tag.p.a.get('href')})
	logging.debug(actor)
	return actor



# 获取演员信息
def get_actors_info(dict):
	global baseUrl
	global items

	url=baseUrl.format(dict['href'])
	logging.debug(url)
	html=get_one_page(url)
	soup=BeautifulSoup(html,'html.parser')
	actorinfo=soup.div.find(id='gaiyao').find(class_='tn-box-content tn-widget-content tn-corner-bottom').text
	# 正则匹配分割字符串
	actorinfo=re.split('\s\s+|\r\n|\n|:',actorinfo)
	logging.info(actorinfo)
	dict['info']=actorinfo
	logging.debug(dict)
	with lock:
		items.append((dict['name'],dict['role'],dict['info']))

logging.basicConfig(level=logging.INFO)
baseUrl="http://www.tvzn.com/{}"
lock=threading.Lock()
items=[]

if __name__=='__main__':
	start_time=time.time()
	threads=[]
	actors=get_actors(get_one_page(baseUrl.format('/14784/yanyuanbiao.html')))
	for actor in actors:
		threads.append(threading.Thread(target=get_actors_info,args=(actor,),name='T'+actor['name']))
	for t in threads:
		t.start()
	for t in threads:
		t.join()
	logging.debug(items)
	df=pd.DataFrame(data=items,columns=['name','role','info'])
	df.to_csv('actors_info.csv',index=False,encoding='utf_8_sig')
	end_time=time.time()
	print("Scraping time:%ds"%(round(end_time-start_time,3)))