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
    content=etree.HTML(html)
    # @data-index属性
    areas=content.xpath("//dd[@data-index='0']//div[@class='option-list']/a/text()")
    areas_link=content.xpath("//dd[@data-index='0']//div[@class='option-list']/a/@href")
    logging.info(areas)
    for i in range(1,len(areas)):
        if areas_link[i][0]=="/":
            url = 'https://bj.lianjia.com' + areas_link[i]
        else:
            url=areas_link[i]
        html=get_one_page(url)
        totalpage=re.findall("page-data=\'{\"totalPage\":(\d+),\"curPage\"",html)
        logging.info(totalpage)
        totalpage=int(totalpage[0]) if totalpage!=[] else 0
        logging.info("{}区域有{}页".format(areas[i],totalpage))


def main():
    logging.basicConfig(level=logging.INFO)
    start=time.time()
    url="https://bj.lianjia.com/zufang"
    html=get_one_page(url)
    get_areas(html)
    
    end=time.time()
    print("Scraping time:%d minutes"%((end-start)//60))


if __name__=='__main__':
    main()