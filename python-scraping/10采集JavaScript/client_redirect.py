

""" 处理客户端重定向 """

from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException

def waitForLoad(dirver):
    # elem=driver.find_element_by_tag_name("html")
    elem=driver.find_element_by_id("content")
    count=0
    while True:
        count+=1
        if count>20:
            print("Timing out after 10 seconds and returning")
            return
        time.sleep(.5)
        try:
            # elem==driver.find_element_by_tag_name("html")
            elem=driver.find_element_by_id("content")
        except StaleElementReferenceException:
            return
        except NoSuchElementException:
            return

driver=webdriver.PhantomJS(executable_path=r"D:\Software\phantomjs-2.1.1-windows\bin\phantomjs")
driver.get("http://pythonscraping.com/pages/javascript/redirectDemo1.html")
waitForLoad(driver)
print(driver.page_source)

