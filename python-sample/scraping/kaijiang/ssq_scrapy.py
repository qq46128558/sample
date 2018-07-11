#!/usr/bin/env python3

'爬取2018年的福彩双色球信息'

import requests
from bs4 import BeautifulSoup
import xlwt
import time
import logging
import re
import pandas as pd

logging.basicConfig(level=logging.INFO)

# 获取一页的内容
def get_one_page(url):
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
    }
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        return response.text
    return None

# 解析一页内容，数据结构化
def parse_one_page(html):
    soup=BeautifulSoup(html,'lxml')
    pos=0
    for item in soup.select('tr')[2:-1]:
        try:
            luckyguy=int(item.select('td strong')[pos+1].text)
            region=re.search(r'\((.*)\)',item.select('td')[pos+4].text)
            yield {
                'time':item.select('td')[pos].text,
                'issue':item.select('td')[pos+1].text,
                # [2, 18, 19, 24, 25, 33, 11]
                # 将后面的item list逐个传入map指定的函数
                # 'digits':list(map(lambda x:int(x.text),item.select('td em'))),
                # 转字符串'2,18,19,24,25,33,11'
                'digits':','.join(map(lambda x:x.text,item.select('td em'))),
                'sales':int(item.select('td strong')[pos].text.replace(',','')),
                'luckyguy':luckyguy,
                # ['京', '皖', '鲁', '琼..']
                # '2\r\n          (浙 闽)\r\n          ' =>['浙', '闽']
                # 'region':re.search(r'\((.*)\)',item.select('td')[pos+4].text).group(1).split(' '),
                # 转字符串'京, 皖, 鲁, 琼'
                'region':'' if luckyguy==0 or not region  else ','.join(re.split(r'\.+',region.group(1))[0].split(' '))
            }
        except:
            logging.error(item)
            logging.info(item.select('td')[pos+4].text)
            yield {'time':'','issue':'','digits':'','sales':'','luckyguy':'','region':''}

def main():
    # 所有双色球开奖信息
    ssq_info=[]
    base_url="http://kaijiang.zhcw.com/zhcw/html/ssq/list_{}.html"
    # 取总页数
    html=get_one_page(base_url.format(1))
    soup=BeautifulSoup(html,'html.parser')
    totalpage=int(soup.find('p',{'class':'pg'}).strong.get_text())
    for i in range (1,totalpage+1):
        html=get_one_page(base_url.format(i))
        if html:
            # logging.info(next(parse_one_page(html)))
            # print(list(parse_one_page(html)))
            ssq_info+=(list(parse_one_page(html)))
    df=pd.DataFrame.from_dict(ssq_info)
    df.to_csv('ssq_info.csv',index=False,encoding='gb18030')
    print('已保存为csv文件.') 

if __name__=='__main__':
    main()