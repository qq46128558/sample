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

# 获取一个页面
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
				list_cat.append({"name":a.string,"url":a.attrs['href']})
	return list_cat

# 获取城市url信息
def get_city(list_cat):
	baseurl="http://www.mafengwo.cn"
	# 定义list存放城市的url
	list_city=[]
	# 循环省级目的地
	# 测试用
	# for i in range(0,1):
	for i in range(0,len(list_cat)):
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
		# 统计城计数
		city_count=0
		while True:
			try:
				tags=soup.find_all('a',attrs={'data-type':'目的地'})
				# div里面有p
				'''.contents 和 .children 属性仅包含tag的直接子节点'''
				logging.debug([tag.div.contents[0].replace('\n','').replace(' ','').strip() for tag in tags])
				city_count+=len(tags)

				# 获取城市名称及cityid
				# ('拉市海','15894'),
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
				time.sleep(4)

				soup=BeautifulSoup(driver.page_source,'html.parser')
				
			except Exception as e:
				logging.error(str(e))
				logging.info('已爬取城市ID数:{}'.format(city_count))
				break
		driver.close()
	return list_city


if __name__=='__main__':
	logging.basicConfig(level=logging.INFO)
	baseurl="http://www.mafengwo.cn/mdd/"
	html=get_one_page(baseurl)
	list_city=[]
	try:
		list_city=get_city(get_category(html))
	except Exception as e:
		logging.error(str(e))
	finally:
		df=pd.DataFrame(data=list_city,columns=['name','data-id'])
		df.to_csv('city_id.csv',index=False,encoding='gb18030')
