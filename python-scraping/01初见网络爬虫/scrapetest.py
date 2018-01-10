
# 查找Python的request模块(在urllib库里),只导入urlopen一个函数
from urllib.request import urlopen
# 引入BeautifulSoup增强功能
from bs4 import BeautifulSoup
from urllib.error import HTTPError

def getTitle(url):
    # 处理异常
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    try:
        # 输出在域名为http://pythonscraping.com的服务器上<网络应用根地址>/pages文件夹里的HTML文件page1.html的源代码
        # print(html.read())
        # 利用BeautifulSoup读取结构化的信息
        bsObj=BeautifulSoup(html.read(),'html.parser')
        # 任何HTML或XML文件的任意节点信息都可以被提取出来,只要目标信息的旁边或附近有标记就行
        title=bsObj.body.h1
    except AttributeError as e:
        return None
    return title

# 具有周密的异常处理功能的通用函数,会让快速稳定地网络数据采集变得简单易行
title=getTitle("http://www.pythonscraping.com/pages/page1.html")
if title==None:
    print("Title could not be found")
else:
    print(title)


