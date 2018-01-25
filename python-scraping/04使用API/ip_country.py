#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'查询维基百科编辑者地理位置'
# 首先做一个采集维基百科的基本程序，寻找编辑历史页面，然后把编辑历史里面的 IP 地址找出来

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
import json
from urllib.error import HTTPError

random.seed(datetime.datetime.now())
def getLink(articleUrl):
    html=urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj=BeautifulSoup(html,'html.parser')
    return bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))

def getHistoryIPs(pageUrl):
    # 编辑历史页面URL链接格式是：
    # http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    pageUrl=pageUrl.replace("/wiki/","")
    historyUrl="http://en.wikipedia.org/w/index.php?title="+pageUrl+"&action=history"
    print("History url is: "+historyUrl)
    html=urlopen(historyUrl)
    bsObj=BeautifulSoup(html,'html.parser')
    # 找出class属性是"mw-anonuserlink"的链接
    # 它们用IP地址代替用户名
    ipAddresses=bsObj.findAll("a",{"class":"mw-anonuserlink"})
    # Python 的集合是无序的,用集合的一个好处就是它不会储存重复值, Python 集合就是值为 None 的词典，用的是哈希表结构
    addressList=set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList

def get_country(ip):
    try:
        reponse=urlopen("https://freegeoip.net/json/"+ip).read().decode('utf-8')
    except HTTPError as e:
        return "Unknow country"
    reponseJson=json.loads(reponse)
    return reponseJson.get("country_name")

links=getLink("/wiki/Python_(programming_language)")

while(len(links)>0):
    for link in links:
        print("----------------")
        historyIPs=getHistoryIPs(link.attrs["href"])
        for historyIP in historyIPs:
            print(historyIP,get_country(historyIP))
    newLink=links[random.randint(0,len(links)-1)].attrs["href"]
    links=getLinks(newLink)
