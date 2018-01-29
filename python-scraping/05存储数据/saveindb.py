#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'爬维基百科信息存到mysql'

'''
CREATE TABLE scraping;
CREATE TABLE pages(id BIGINT(7) NOT NULL AUTO_INCREMENT,title VARCHAR(200),content VARCHA(10000),created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,PRIMARY KEY(id));
INSERT INTO pages(title,content)VALUES("Test page title","This is some test page content. It can be up to 10,000 characters long.");
ALTER DATABASE scraping CHARACTER SET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
ALTER TABLE pages CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE pages CHANGE title title VARCHAR(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE pages CHANGE content content VARCHAR(10000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
'''

import pymysql,re,random,datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup

# charset='utf8' 要增加到连接字符串里。这是让连接 conn 把所有发送到数据库的信息都当成 UTF-8 编码格式（当然，前提是数据库默认编码已经设置成 UTF-8）。
conn=pymysql.connect(host='127.0.0.1',user='root',passwd='root',db='mysql',charset='utf8')
cur=conn.cursor()
cur.execute('USE scraping')

random.seed(datetime.datetime.now())

def store(title,content):
    cur.execute("INSERT INTO pages(title,content) VALUES (\"%s\",\"%s\")",(title,content))
    cur.connection.commit()

def getLinks(articleUrl):
    html=urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj=BeautifulSoup(html,'html.parser')
    title=bsObj.find("h1").get_text()
    content=bsObj.find("div",{"id":"mw-content-text"}).find("p").get_text()
    store(title,content)
    return bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))

links=getLinks("/wiki/Kevin_Bacon")
try:
    while len(links)>0:
        newArticle=links[random.randint(0,len(links)-1)].attrs['href']
        print(newArticle)
        links=getLinks(newArticle)
finally:
    cur.close()
    conn.close()
