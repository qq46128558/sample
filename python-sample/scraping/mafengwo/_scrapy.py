#!/usr/bin/env python3

'马蜂窝城市旅游数据分析'

import logging
from urllib.request import urlopen
import urllib.request as request
from bs4 import BeautifulSoup
import re
# 动态数据爬取
from selenium import webdriver
import time
import pandas as pd
# 引入多线程
import threading


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


# 获取省级目的地url信息
def get_category(html):
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
	list_cat=[]
	# 循环大目的地
	for i in range(0,len(list_tag)):
		# 循环里面的dt tag
		for tag in list_tag[i]:
			# 查找dt里面的a tag
			for a in tag.find_all('a'):
				# 找到省名及url名,写入list
				m=re.match(r'/travel-scenic-spot/mafengwo/(\d+).html',a.attrs['href'])
				list_cat.append({"name":a.string,"url":a.attrs['href'],"data-id":m.group(1) if m else 0})
	return list_cat

# 获取城市url信息
def get_city(list_cat):
	# 全局list,防止爬取中断后无数据
	global list_city
	baseurl="http://www.mafengwo.cn"
	# 循环省级目的地
	# 测试用
	# for i in range(0,1):
	for i in range(0,len(list_cat)):
		soup=BeautifulSoup(get_one_page(baseurl+list_cat[i]["url"]),'html.parser')
		time.sleep(1)
		# 统计城市数
		city_count=0
		# province=soup.find('div',class_='title').h1.string
		province=list_cat[i]['name']
		province_id=list_cat[i]['data-id']
		
		# 如果不存在目的地，则直接返回当前城市
		if soup.find('a',href=re.compile('/mdd/citylist'))==None:
			logging.info('Single city:{} data-id:{}'.format(province,province_id))
			with lock:
				list_city.append((province,province_id))
			continue

		# 用Selenium执行JavaScript
		# driver=webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chrome")
		driver=webdriver.PhantomJS(executable_path=r"D:\Software\phantomjs-2.1.1-windows\bin\phantomjs")
		driver.maximize_window()
		url=baseurl+list_cat[i]["url"].replace('travel-scenic-spot/mafengwo','mdd/citylist')
		logging.info(url)
		driver.get(url)
		# driver.page_source 也是读过一次就空了
		soup=BeautifulSoup(driver.page_source,'html.parser')
		logging.info(soup.title.string)
		
		while True:
			try:
				tags=soup.find_all('a',attrs={'data-type':'目的地'})
				# div里面有p
				'''.contents 和 .children 属性仅包含tag的直接子节点'''
				logging.debug([tag.div.contents[0].replace('\n','').replace(' ','').strip() for tag in tags])
				city_count+=len(tags)

				# 获取城市名称及cityid
				# ('拉市海','15894'),
				# with lock 相当于获取锁与释放锁
				with lock:
					list_city=list_city+[(tag.div.contents[0].replace('\n','').replace(' ','').strip(),tag.get('data-id')) for tag in tags]

				# 未理解
				js="var q=document.documentElement.scrollTop=800"
				driver.execute_script(js)
				# time.sleep(2)

				# 报错1:Element is not currently visible and may not be manipulated
				# 解决:需要加这一句
				# 报销2:Compound class names not permitted
				# 解决:不能用组合的class name
				driver.find_element_by_class_name('pg-next').click()
				
				# 需要暂停2秒让其加载页面,否则报错:Element is no longer attached to the DOM"
				time.sleep(2)

				soup=BeautifulSoup(driver.page_source,'html.parser')
				
			except Exception as e:
				logging.error(str(e))
				logging.info('已爬取{}城市ID数:{}'.format(province,city_count))
				break
			finally:
				# lock.release()
				pass

		driver.close()

# 多线程爬取
def run_thread_by_cat(html):
	global list_city
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

	# 多个线程爬取7个大类目的地
	threads=[]
	for i in range(0,len(list_tag)):
		list_cat=[]
		# 循环里面的dt tag
		for tag in list_tag[i]:
			# 查找dt里面的a tag
			for a in tag.find_all('a'):
				# 找到省名及url名,写入list
				m=re.match(r'/travel-scenic-spot/mafengwo/(\d+).html',a.attrs['href'])
				list_cat.append({"name":a.string,"url":a.attrs['href'],"data-id":m.group(1) if m else 0})
		# 多线程
		threads.append(threading.Thread(target=get_city,args=(list_cat,),name='T'+str(i)))
	for t in threads:
		t.start()
	for t in threads:
		t.join()


lock=threading.Lock()

if __name__=='__main__':
	logging.basicConfig(level=logging.INFO)
	baseurl="http://www.mafengwo.cn/mdd/"
	html=get_one_page(baseurl)
	list_city=[]
	try:
		run_thread_by_cat(html)
	except Exception as e:
		logging.error(str(e))
	finally:
		# 四个直辖市
		list_city.append(('北京','10065'))
		list_city.append(('上海','10099'))
		list_city.append(('重庆','10208'))
		list_city.append(('天津','10320'))
		df=pd.DataFrame(data=list_city,columns=['name','data-id'])
		df.to_csv('city_id.csv',index=False,encoding='gb18030')
