#!/usr/bin/env python3

'北京链家租房数据'

import logging
import requests
import time
import re
# 解析网页，用xpath表达式与正则表达式一起来获取网页信息，相比bs4速度更快
from lxml import etree
# from urllib.request import urlopen
# from urllib.request import Request

def get_one_page(url):
    headers={"User-Agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}
    response=requests.get(url,headers=headers)
    # html=urlopen(Request(url,headers=headers))
    if response.status_code==200:
        return response.text
    return None

def get_areas(html):
    pass

def main():
    start=time.time()
    url="https://bj.lianjia.com/zufang"
    html=get_one_page(url)
    get_areas(html)
    
    end=time.time()
    print('Scraping time:%d minutes'%(end-start)//60)


if __name__=='__main__':
    main()