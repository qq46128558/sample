#!/usr/bin/env python3

'selenium动态数据爬取 示例:马蜂窝'

import logging
from selenium import webdriver
import time
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)

driver=webdriver.PhantomJS(executable_path=r"D:\Software\phantomjs-2.1.1-windows\bin\phantomjs")
driver.maximize_window()
url="http://www.mafengwo.cn/mdd/citylist/10183.html"
driver.get(url)

soup=BeautifulSoup(driver.page_source,'html.parser')
logging.info(soup.title.string)
count=0
while True:
	try:
		tags=soup.find_all('a',attrs={'data-type':'目的地'})
		count+=len(tags)
		logging.info([tag.div.text.replace(' ','').replace('\n','') for tag in tags])
		
		# 未理解
		js="var p=document.documentElement.scrollTop=800"
		driver.execute_script(js)
		
		# 单击下一页
		driver.find_element_by_class_name('pg-next').click()
		
		time.sleep(2)
		soup=BeautifulSoup(driver.page_source,'html.parser')

	except Exception as e:
		logging.info(str(e))
		break;

print('Total city: %s'%count)

