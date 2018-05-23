
""" 在Python中用Selenium执行JavaScript 使用BeautifulSoup解析"""

from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver=webdriver.PhantomJS(executable_path=r"D:\Software\phantomjs-2.1.1-windows\bin\phantomjs")

driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3)

# print(driver.find_element_by_id('content').text)
# 如果你还是想用 BeautifulSoup 来解析网页内容，可以用 WebDriver 的 page_source 函数返回页面的源代码字符串。
page_source=driver.page_source
bsObj=BeautifulSoup(page_source,'html.parser')
print(bsObj.find(id='content').get_text())

driver.close()
