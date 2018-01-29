#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'use pymysql'
'''
CREATE TABLE scraping;
CREATE TABLE pages(id BIGINT(7) NOT NULL AUTO_INCREMENT,title VARCHAR(200),content VARCHA(10000),created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,PRIMARY KEY(id));
INSERT INTO pages(title,content)VALUES("Test page title","This is some test page content. It can be up to 10,000 characters long.");
'''

import pymysql

# 连接对象
conn=pymysql.connect(host="127.0.0.1",user="root",passwd="root",db="mysql")
# 光标对象
cursor=conn.cursor()
cursor.execute("USE scraping")
cursor.execute("SELECT * FROM pages WHERE id=1")
print(cursor.fetchone())
# 用完光标和连接之后，千万记得把它们关闭。如果不关闭就会导致连接泄漏（connection leak），造成一种未关闭连接现象，即连接已经不再使用，但是数据库却不能关闭，因为数据库不能确定你还要不要继续使用它。
cursor.close()
conn.close()
