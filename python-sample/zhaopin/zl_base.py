#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Python爬虫抓取智联招聘（基础版）'
'https://mp.weixin.qq.com/s/6QSboFmqP0giiY65AsiNkQ'

__author__='C与Python实战'

import re
import csv
import requests
from tqdm import tqdm
from urllib.parse import urlencode
from requests.exceptions import RequestException
import math

def get_one_page(city,keyword,region,page):
    """ 获取网页html内容并返回 """
    paras={
        'jl':city,          # 搜索城市
        'kw':keyword,       # 搜索关键词 
        'isadv':0,          # 是否打开更详细搜索选项
        'isfilter':1,       # 是否对结果过滤
        'p':page,           # 页数
        're':region         # region的缩写，地区，2005代表海淀
    }
    # 区域不限
    if region==0:
        paras.pop('re')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Host': 'sou.zhaopin.com',
        'Referer': 'https://www.zhaopin.com/',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    # urlencode: jl=city&kw=keyword...
    url='https://sou.zhaopin.com/jobs/searchresult.ashx?'+urlencode(paras)
    try:
        # 获取网页内容，返回html数据
        response=requests.get(url,headers=headers)
        # 通过状态码判断是否获取成功
        if response.status_code==200:
            return response.text
        return None
    except RequestException as e:
        return None

# 获取职位个数
def parse_position_count(html):
    # with open('./temp.txt','w',encoding='gb18030') as f:
    #     f.write(html)
    pattern=re.compile(r'<span class="search_yx_tj">.*?<em>(\d*)</em>',re.S)
    m=pattern.search(html)
    if m==None:
        return 0
    else:
        return int(m.groups(0)[0])

def parse_one_page(html):
    """ 解析HTML代码，提取有用信息并返回 """
    # 正则表达式进行解析
    pattern = re.compile('<a style=.*? target="_blank">(.*?)</a>.*?'       # 匹配职位信息
       '<td class="gsmc"><a href="(.*?)" target="_blank">(.*?)</a>.*?'     # 匹配公司网址和公司名称
       '<td class="zwyx">(.*?)</td>.*?'                                       # 匹配月薪      
       '<td class="gzdd">(.*?)</td>', re.S)                               
    # 匹配所有符合条件的内容
    items=re.findall(pattern,html)
    # ('网站开发工程师', 'http://company.zhaopin.com/CC276898035.htm', '珠海横琴天汇星实业有限公司', '4001-6000')
    for item in items:
        job_name=item[0]
        job_name=job_name.replace('<b>','')
        job_name=job_name.replace('</b>','')
        yield{
            '职位':job_name,
            # 'website':item[1],
            '公司':item[2],
            '月薪':item[3],
            '地点':item[4]
        }
        
def write_csv_file(path,headers,rows):
    """ 将表头和行写入csv文件 """
    # 加入encoding防止中文写入报错
    # newline参数防止每写入一行都多一个空行
    with open(path,'a',encoding='gb18030',newline='') as f:
        f_csv=csv.DictWriter(f,headers)
        # f_csv=csv.writer(f)
        f_csv.writeheader()
        f_csv.writerows(rows)

def main(city,keyword,region,pages):
    """ 主函数 """
    filename='zl_'+city+'_'+keyword+'.csv'
    headers=['职位','公司','月薪','地点']
    # 进行进度显示
    jobs=[]
    for i in tqdm(range(pages)):
        """ 获取该页中所有职位信息，写入csv文件 """
        html=get_one_page(city,keyword,region,i)
        items=parse_one_page(html)
        for item in items:
            jobs.append(item)
    write_csv_file(filename,headers,jobs)

if __name__=='__main__':
    # 3185保税区 3184高新区 3183横琴新区 3182金湾区 3181斗门区 3180香洲区 0不限
    city,keyword,region='珠海','PHP',3184
    # 获取职位个数
    html=get_one_page(city,keyword,region,1)
    pcount=parse_position_count(html)
    # 每页60个
    pages=math.ceil(pcount/60)
    main(city,keyword,region,pages)
    