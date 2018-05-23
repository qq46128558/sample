
""" 用 id 是 loadedButton 的按钮检查页面是不是已经完全加载 """

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

executable_path=r'D:\Software\phantomjs-2.1.1-windows\bin\phantomjs'
driver=webdriver.PhantomJS(executable_path=executable_path)
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
try:
    element=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"loadedButton")))
finally:
    print(driver.find_element_by_id('content').text)
    driver.close()
