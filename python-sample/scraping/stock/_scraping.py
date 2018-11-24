#!/usr/bin/env python3

'爬取全国所有A股/港股/新三板上市公司信息'

# https://www.makcyun.top/web_scraping_withpython2.html

import logging
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
from urllib.parse import urlencode # 编码 URL 字符串
import numpy as np

logging.basicConfig(level=logging.INFO)

start_time=time.time() #计算程序运行时间

def get_one_page(i):
    try:
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        }
        paras={
            'reportTime':'2017-12-31', #可以改报告日期，比如2018-6-30获得的就是该季度的信息
            'pageNum': i  #页码
        }
        url = 'http://s.askci.com/stock/a/?' + urlencode(paras)
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.text
        return None
    except requests.RequestException:
        print("Scraping failed")

def parse_one_page(html):
    soup=BeautifulSoup(html,'lxml')
    content = soup.select('#myTable04')[0] #[0]将返回的list改为bs4类型
    df=pd.read_html(content.prettify(),header=0)[0]
    # prettify()优化代码,[0]从pd.read_html返回的list中提取出DataFrame]
    df.to_csv(r'1.csv', mode='a', encoding='utf_8_sig', header=1, index=0)
    # list=np.array(df).tolist()
    # logging.info(list)

def main(page):
    html=get_one_page(page)
    parse_one_page(html)
    logging.info('Page %s scraping finished'%page)

from multiprocessing import Pool
if __name__=='__main__':
    pool=Pool(4)
    pool.map(main,[i for i in range(1,179)])
    print('Scraping time: %.2fs'%(time.time()-start_time))

'''
pandas.read_html(io, match='.+', flavor=None, header=None, index_col=None, skiprows=None, attrs=None, parse_dates=False, tupleize_cols=None, thousands=', ', encoding=None, decimal='.', converters=None, na_values=None, keep_default_na=True, displayed_only=True)

常用的参数：
io:可以是url、html文本、本地文件等；
flavor：解析器；
header：标题行；
skiprows：跳过的行；
attrs：属性，比如 attrs = {'id': 'table'}；
parse_dates：解析日期

注意：返回的结果是**DataFrame**组成的**list**。
'''