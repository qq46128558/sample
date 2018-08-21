#!/usr/bin/env python3

'获取城市信息:印象游记/餐饮'

import logging
import urllib.request as request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import threading
import pandas as pd
import time
import random

# 获取一个页面
def get_one_page(url):
	headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
	myrequest=request.Request(url,headers=headers)
	logging.debug(myrequest)
	# INFO:root:<urllib.request.Request object at 0x0000020633C26CF8>
	html=urlopen(myrequest)
	# read()一次后html就不能再read()
	html=html.read()
	logging.debug(type(html))
	# INFO:root:<class 'bytes'>
	return html

# 获取印象游记信息
def get_city_yj(df):
	global items
	url="http://www.mafengwo.cn/xc/{}/"
	logging.debug(df.name.count())
	dict={}
	# 记录出错的城市
	error_i=0 
	try:
		# 城市循环
		for i in range(0,df.name.count()):
			error_i=i
			# 初始化城市信息
			dict["data-id"]=df['data-id'][i]
			dict["城市"]=df['name'][i]
			dict["印象"]=''
			dict['城市游记']=0
			dict['印象游记']=0
			dict['景点游记']=0
			dict['餐饮游记']=0
			dict['购物游记']=0
			dict['娱乐游记']=0

			# 开始爬取行程页的印象
			soup=BeautifulSoup(get_one_page(url.format(str(df['data-id'][i]))),'html.parser')
			soup_yx=soup.find('div',class_="m-tags")
			if soup_yx==None:
				logging.info("city:{},没有印象记录".format(df['name'][i]))
			else:
				tags=soup_yx.find('div',class_="bd").find_all('a')
				# <a href="/jd/10269/13156.html" target="_blank">岛<em> 335</em></a>
				for tag in tags:
					logging.debug(tag.get('href')[1:3])
					text=tag.text.split()[0]
					# 发现有重复的印象,导致印象游记比城市游记多,加个重复排除
					if text not in dict['印象']:
						dict["印象"]+=(text if text!='更多>>' else '') + ' '
						dict["印象游记"]+=int(tag.contents[1].string) if len(tag.contents)>1 else 0
						dict["景点游记"]+=int(tag.contents[1].string) if tag.get('href')[1:3]=="jd" and len(tag.contents)>1 else 0
						dict["餐饮游记"]+=int(tag.contents[1].string) if tag.get('href')[1:3]=='cy' and len(tag.contents)>1 else 0
						dict["购物游记"]+=int(tag.contents[1].string) if tag.get('href')[1:3]=='gw' and len(tag.contents)>1 else 0
						dict["娱乐游记"]+=int(tag.contents[1].string) if tag.get('href')[1:3]=='yl' and len(tag.contents)>1 else 0

				# 爬取城市游记
				soup_yj=BeautifulSoup(get_one_page("http://www.mafengwo.cn/yj/{}/2-0-1.html".format(str(df['data-id'][i]))),'html.parser')
				soup_yj=soup_yj.find('span',class_='count')
				# 爬取页面上的统计条数
				dict['城市游记']=int(soup_yj.find_all('span')[1].text) if soup_yj!=None else 0

			time.sleep(1)
			# 爬取完成
			logging.info("city:{},url:{} 爬取行程页印象完成".format(df['name'][i],url.format(str(df['data-id'][i]))))
			# 这里strip要传空格
			dict["印象"]=dict["印象"].strip(' ')
			logging.info(dict)
			# 存入items list,加锁
			with lock:
				# items.append((dict.values()))
				items.append((dict['data-id'],dict["城市"],dict["印象"],dict['城市游记'],dict['印象游记'],dict['景点游记'],dict['餐饮游记'],dict['购物游记'],dict['娱乐游记']))
			time.sleep(1)
			# ERROR:root:安庆:12058,[WinError 10054] 远程主机强迫关闭了一个现有的连接。
	except Exception as e:
		# 江都:84556,
		error_s="{}:{},{}".format(df['name'][error_i],df['data-id'][error_i],str(e))
		logging.error(error_s)
		with open ('error.log','a',encoding='utf-8',errors='ignore') as f:
			f.write(error_s+"\n")

# 获取城市特色美食
def get_city_cy(df):
	global items
	url="http://www.mafengwo.cn/cy/{}/gonglve.html"
	logging.debug(df.name.count())
	dict={}
	# 记录出错的城市
	error_i=0 
	try:
		# 城市循环
		for i in range(0,df.name.count()):
			error_i=i
			# 初始化城市信息
			dict["data-id"]=df['data-id'][i]
			dict["城市"]=df['name'][i]
			dict["美食"]='没有'
			dict['票数']=0
			soup=BeautifulSoup(get_one_page(url.format(str(df['data-id'][i]))),'html.parser')
			soup_cy=soup.find('ol',class_="list-rank")
			if soup_cy==None:
				logging.info("city:{},没有特色美食".format(df['name'][i]))
				with lock:
					# items.append((dict.values()))
					items.append((dict['data-id'],dict["城市"],dict["美食"],dict['票数']))
			else:
				tags=soup_cy.find_all('li')
				for tag in tags:
					logging.debug(tag)
					dict["美食"]=tag.find('h3').text
					dict['票数 ']=int(tag.find('span',class_='trend').text) if tag.find('span',class_='trend')!=None else 1
					logging.info(dict)
					# 存入items list,加锁
					with lock:
						# items.append((dict.values()))
						items.append((dict['data-id'],dict["城市"],dict["美食"],dict['票数']))

			# 爬取完成
			logging.info("city:{},url:{} 爬取美食完成".format(df['name'][i],url.format(str(df['data-id'][i]))))
			# 随机暂停
			time.sleep(random.choice(range(3)))
			# ERROR:root:安庆:12058,[WinError 10054] 远程主机强迫关闭了一个现有的连接。
	except Exception as e:
		# 江都:84556,
		error_s="{}:{},{}".format(df['name'][error_i],df['data-id'][error_i],str(e))
		logging.error(error_s)
		with open ('error.log','a',encoding='utf-8',errors='ignore') as f:
			f.write(error_s+"\n")



# 存放爬取的信息(全局多线程用)
items=[]
lock=threading.Lock()

if __name__=='__main__':
	start=time.time()
	logging.basicConfig(level=logging.INFO)
	df=pd.read_csv('city_id.csv',encoding='gb18030')
	# 三千多个城市,分四个线程
	threads=[]
	for x,y in [(0,1000),(1000,2000),(2000,3000),(3000,df['name'].count())]:
		# 注意需重新索引
		# 印象游记(已获取)
		# threads.append(threading.Thread(target=get_city_yj,args=(df.iloc[x:y].reset_index(drop=True),),name='T'+str(y)))

		# 特色美食
		threads.append(threading.Thread(target=get_city_cy,args=(df.iloc[x:y].reset_index(drop=True),),name='T'+str(y)))

	for t in threads:
		t.start()
	for t in threads:
		t.join()

	# 保存爬取记录

	# 印象游记(已获取)
	# df=pd.DataFrame(data=items,columns=["data-id","城市","印象",'城市游记','印象游记','景点游记','餐饮游记','购物游记','娱乐游记'])
	# df.to_csv('city_yj.csv',index=False,encoding='gb18030')

	# 特色美食
	df=pd.DataFrame(data=items,columns=["data-id","城市","美食","票数"])
	df.to_csv('city_cy.csv',index=False,encoding='gb18030')

	end=time.time()
	print('Scraping time:{} minutes'.format((end-start)//60))