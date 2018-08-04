#!/usr/bin/env python3

'抓取风雨咒猫眼电影评论'

# http://m.maoyan.com/mmdb/comments/movie/1217513.json?_v_=yes&offset=1

import logging
import requests
import json
import pandas as pd
import time

logging.basicConfig(level=logging.INFO)

def get_one_page(url):
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
    }
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        return response.text
    return None

def parse_one_page(html):
    try:
        data=json.loads(html)['cmts']
        for item in data:
            yield{
                'comment':item['content'],
                'date':item['time'].split(' ')[0],
                'rate':item['score'],
                'city':item['cityName'],
                'nickname':item['nickName'],

            }
    except Exception as e:
        logging.error(str(e))
        return {'comment':'','date':'','rate':'','city':'','nickname':''}

def save_to_csv(items):
    df=pd.DataFrame(data=items,columns=['评论','日期','评分','城市','昵称'])
    df.to_csv('the_wind_guardians.csv',index=False,encoding='gb18030')

def main():
    baseurl="http://m.maoyan.com/mmdb/comments/movie/1217513.json?_v_=yes&offset={}"
    try:
        items=[]
        for i in range(1,1001):
            html=get_one_page(baseurl.format(i))
            logging.info('Scraping page {}'.format(i))
            for item in parse_one_page(html):
                items.append(list(item.values()))
            if i<1000:
                time.sleep(1)
        save_to_csv(items)
    except Exception as e:
        logging.error(str(e))

if __name__=='__main__':
    main()


