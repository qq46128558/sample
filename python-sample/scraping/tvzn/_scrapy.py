#!/usr/bin/env python3

'爬取电视指南网延禧攻略信息'
'多线程|正则分割|正则替换'
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
	# 用encode查看换行符
	logging.debug(soup.div.find(id='gaiyao').find(class_='tn-box-content tn-widget-content tn-corner-bottom').encode('gbk'))

	# 正则替换: 分开处理\r\n与\n
	actorinfo=re.sub('\r\n','<br>',actorinfo)
	actorinfo=re.sub('\n','',actorinfo)
	actorinfo=actorinfo.replace(' ','')
	
	
	# 正则匹配分割字符串:<br>及:分割
	actorinfo=re.split('<br>|:',actorinfo)
	logging.info(actorinfo)
	dict['身高']=actorinfo[4]
	dict['体重']=actorinfo[6]
	dict['生日']=actorinfo[10]
	dict['星座']=actorinfo[12]
	logging.debug(dict)
	with lock:
		items.append((dict['name'],dict['role'],dict['身高'],dict['体重'],dict['生日'],dict['星座']))

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
	df=pd.DataFrame(data=items,columns=['name','role','身高','体重','生日','星座'])
	df.to_csv('actors_info.csv',index=False,encoding='utf_8_sig')
	end_time=time.time()
	print("Scraping time:%ds"%(round(end_time-start_time,3)))