#!/usr/bin/env python3

'抓取猫眼电影评论'

# 打开猫眼网页（http://maoyan.com/films/248566）只有寥寥几个评论，那它的数据会不会是通过json格式保存到服务器中呢？无奈只能通过抓包猫眼APP来找其数据接口
# 最后，发现其数据接口为：http://m.maoyan.com/mmdb/comments/movie/248566.json?_v_=yes&offset=1，其中258566属于电影的专属id，offset代表页数
# 最后检验，这个接口只给展示1000页数据

# 最多1000页，数据太多，基本1000页都是同一天的，所以需要每天爬，此处略

import requests
import json
import time
import random
import logging
import pandas as pd

logging.basicConfig(level=logging.INFO)

#下载一页数据
def get_one_page(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
    }
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        return response.text
    return None

# 解析一页数据
def parse_one_page(html):
    try:
        data=json.loads(html)['cmts']
        # by peter：热门短评
        # data+=json.loads(html)['hcmts']
        for item in data:
            yield {
                'comment':item['content'],
                'date':item['time'].split(' ')[0],
                'rate':item['score'],
                'city':item['cityName'],
                'nickname':item['nickName'],
            }
    except Exception as e:
        logging.error(str(e))
        return {'comment':'','date':'','rate':'','city':'','nickname':''}


# 保存数据到文本文档
def save_to_txt():
    baseurl="http://m.maoyan.com/mmdb/comments/movie/248566.json?_v_=yes&offset="
    try:
        # 先清空
        with open ('hidden_man.txt','w',encoding='utf-8') as f:
            f.write('')
        # 此处可修改页数:1001
        for i in range(1,2):
            url=baseurl+str(i)
            html=get_one_page(url)
            for item in parse_one_page(html):
                with open ('hidden_man.txt','a',encoding='utf-8') as f:
                    f.write(item['date']+','+item['nickname']+','+item['city']+','+str(item['rate'])+','+item['comment']+'\n')
            print('成功保存第%d页'% i)
            # 此处可修改页数:1000
            if i<1:
                time.sleep(5+float(random.randint(1,100))/20)
    except Exception as e:
        logging.error(str(e))

# 保存到csv
def save_to_csv():
    baseurl="http://m.maoyan.com/mmdb/comments/movie/248566.json?_v_=yes&offset="
    try:
        itemdata=[]
        # 此处可修改页数:1001
        # by Peter: <<邪不压正>>实时评论太多，所以第1页可能跟后面几页相同，一天的评论就上万
        for i in range(1,1001):
            url=baseurl+str(i)
            html=get_one_page(url)
            logging.info('采集第{}页...'.format(i))
            for item in parse_one_page(html):
                itemdata.append(tuple(item.values()))
            # 此处可修改页数:1000
            if i<1000:
                time.sleep(5+float(random.randint(1,100))/20)
        df=pd.DataFrame(data=itemdata,columns=['评论','日期','评分','城市','昵称'])
        df.to_csv('hidden_man.csv',index=False,encoding='gb18030')

    except Exception as e:
        logging.error(str(e))

if __name__=='__main__':
    # save_to_txt()
    save_to_csv()



        