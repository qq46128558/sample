
""" 在Python中用Selenium执行JavaScript """

from selenium import webdriver
import time
# from selenium.webdriver.chrome.options import Options

# 报错:  UserWarning: Selenium support for PhantomJS has been deprecated, please use headless versions of Chrome or Firefox instead (可用selenium 2.48.0)
# 用 PhantomJS 库创建了一个新的 Selenium WebDriver
# 依据你的 PhantomJS 安装位置 指明 PhantomJS 可执行文件的路径
driver=webdriver.PhantomJS(executable_path=r"D:\Software\phantomjs-2.1.1-windows\bin\phantomjs")

# 用chrome headless失败,未解决
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# executable_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\"
# driver=webdriver.Chrome(executable_path=executable_path,chrome_options=chrome_options)

driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
# 然后暂停执行 3 秒钟 希望已经加载完成的
time.sleep(3)
# 再查看页面获取
print(driver.find_element_by_id('content').text)
driver.close()
