#!/usr/bin/env python3

""" 爬取拉勾网职位并分析 """


__author__='闲庭信步'
# https://blog.csdn.net/danspace1/article/details/80197106

import requests
import math
def get_json(url,num):
    """ 从网页获取JSON,使用POST请求,加上头部信息 """
    my_headers = {  
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',  
        'Host':'www.lagou.com',  
        'Referer':'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput=',  
        'X-Anit-Forge-Code':'0',  
        'X-Anit-Forge-Token': 'None',  
        'X-Requested-With':'XMLHttpRequest'  
        }
    my_data={
        'first':'true',
        'pn':num,
        'kd':'PHP'
    }
    res=requests.post(url,headers=my_headers,data=my_data)
    res.raise_for_status()
    res.encoding='utf-8'
    # 得到包含职位信息的字典
    page=res.json()
    return page

def main():
    # %E6%B7%B1%E5%9C%B3 深圳
    url="https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false"
    