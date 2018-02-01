#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Mysql里的六度空间游戏(维基百科六度分隔)'

# 设计一个带有两张数据表的数据库来分别存储页面和链接，两张表都带有创建时间和独立的 ID 号
# CREATE DATABASE wikipedia;
# CREATE TABLE `wikipedia`.`pages`(`id` INT NOT NULL AUTO_INCREMENT,`url` VARCHAR(255) NOT NULL,`created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,PRIMARY KEY(`id`));
# CREATE TABLE `wikipedia`.`links`(`id` INT NOT NULL AUTO_INCREMENT,`fromPageId` INT NULL,`toPageId` INT NULL,`created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,PRIMARY KEY(`id`));

from bs4 import BeautifulSoup
import pymysql
import re
from urllib.request import urlopen

conn=pymysql.connect(host='127.0.0.1',user='root',passwd='root',db='mysql',charset='utf8')
cur=conn.cursor()
cur.execute("USE wikipedia")

def insertPageIfNotExists(url):
    cur.execute("SELECT id FROM pages where url=%s",(url))
    if cur.rowcount==0:
        cur.execute("INSERT INTO pages (url) VALUES(%s)",(url))
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]

def insertLink(fromPageId,toPageId):
    cur.execute("SELECT id FROM links where fromPageId=%s and toPageId=%s",(int(fromPageId),int(toPageId)))
    if cur.rowcount==0:
        cur.execute("INSERT INTO links (fromPageId,toPageId) VALUES(%s,%s)",(int(fromPageId),int(toPageId)))
        conn.commit()

pages=set()
def getLinks(pageUrl,recursionLevel):
    global pages
    # 当 recursionLevel 值到 5 的时候，函数会自动返回，不会继续递归。这个限制可以防止数据太大导致内存堆栈溢出。
    if recursionLevel>4:
        return
    pageId=insertPageIfNotExists(pageUrl)
    html=urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj=BeautifulSoup(html,'html.parser')
    # compile处用单引号报错:AttributeError: 'NavigableString' object has no attribute 'attrs'
    for link in bsObj.findAll('a',href=re.compile("^(/wiki/)((?!:).)*$")):
        insertLink(pageId,insertPageIfNotExists(link.attrs['href']))
        if link.attrs['href'] not in pages:
            # 遇到一个新页面,加入集合并搜索里面的词条链接
            newPage=link.attrs['href']
            pages.add(newPage)
            getLinks(newPage,recursionLevel+1)
    
getLinks("/wiki/Kevin_Bacon",0)
cur.close()
conn.close()



