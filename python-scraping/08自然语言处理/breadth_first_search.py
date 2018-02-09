#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
广度优先搜索
breadth-first search
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql

conn=pymysql.connect(host='127.0.0.1',user='root',passwd='root',db='mysql',charset='utf8')
cur=conn.cursor()
cur.execute("USE wikipedia")

class SolutionFound(RuntimeError):
    def __init__(self,message):
        self.message=message

def getLinks(fromPageId):
    cur.execute("SELECT toPageId FROM links WHERE fromPageId=%s",(fromPageId))
    if cur.rowcount==0:
        return None
    else:
        return [x[0] in for x in cur.fetchall()]

def constructDict(currentPageId):
    links=getLinks(currentPageId)
    if links:
        return dict(zip(links,[{}]*len(links)))

