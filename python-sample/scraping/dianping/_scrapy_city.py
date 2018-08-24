#!/usr/bin/env python3

'爬取大众点评城市的链接拼音'

import logging
from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup
import pandas as pd
import time

logging.basicConfig(level=logging.INFO)

def get_one_page(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    html=urlopen(Request(url,headers=headers))
    html=html.read()
    return html

# 获取城市信息——拼音
def get_city_info(html):
    soup=BeautifulSoup(html,'html.parser')
    tags=soup.body.find('div',class_='main-citylist').find_all('a',class_='link onecity')
    list=[[],[]]
    # 补上香港 澳门 台北
    list[0].extend(['香港','澳门','台北'])
    list[1].extend(['hongkong','macau','taipei'])
    for tag in tags:
        # <a href="//www.dianping.com/chengbai" class="link onecity">长白朝鲜族自治县</a>
        logging.debug(tag.text)
        list[0].append(tag.text)
        list[1].append(tag.get('href')[tag.get('href').rfind("/")+1:])

    return {'城市':tuple(list[0]),'拼音':tuple(list[1])}

if __name__=='__main__':
    start=time.time()
    html=get_one_page('http://www.dianping.com/citylist')
    data=get_city_info(html)
    df=pd.DataFrame(data)
    df.to_csv('city.csv',index=False,encoding='gb18030')
    end=time.time()
    print("Scraping time:%ds"%(round(end-start,3)))

