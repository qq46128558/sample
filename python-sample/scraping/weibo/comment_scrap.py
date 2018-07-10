#!/usr/bin/env python3

'爬取微博某博主的评论及用户信息: 结构变化后失败'

import json
import time
import pandas as pd
import requests
import logging

logging.basicConfig(level=logging.INFO)

#获取每条微博评论的url参数
def get_comment_parameter():
    url = 'https://m.weibo.cn/api/container/getIndex?uid=1773294041&luicode=10000011&lfid=100103type%3D1%26q%3D%E7%8E%8B%E8%8F%8A&\featurecode=20000320&type=uid&value=1773294041&containerid=1076031773294041'
    c_r=requests.get(url)
    # by peter:10条微博
    for i in range(2,11):
        c_parameter=(json.loads(c_r.text)["data"]["cards"][i]["mblog"]["id"])
        comment_parameter.append(c_parameter)
    # ['4259957584652713', '4258811936191328', '4258416446800794', '4257334039640707', '4257070428023884', '4256736149277251', '4256177141855565', '4256023138898572', '4255299382401605']
    return comment_parameter

if __name__=="__main__":
    comment_parameter = []#用来存放微博url参数
    comment_url=[]#用来存放微博评论url
    user_id=[]#用来存放user_id
    comment=[]#用来存放评论
    containerid=[]#用来存放containerid
    feature=[]#用来存放用户信息
    id_lose=[]#用来存放访问不成功的user_id

    get_comment_parameter()
    # 获取每条微博评论url
    c_url_base='https://m.weibo.cn/api/comments/show?id='
    for parameter in comment_parameter:
        # edit by peter: 改成1页测试
        for page in range(1,2):#提前知道每条微博只可抓取前100页评论
            c_url=c_url_base+str(parameter)+"&page="+str(page)
            comment_url.append(c_url)
        
    # 获取每个url下的user_id以及评论
    for url in comment_url:
        u_c_r=requests.get(url)
        try:
            for m in range(0,9):#提前知道每个url会包含9条用户信息
                one_id=json.loads(u_c_r.text)["data"]["data"][m]["user"]["id"]
                user_id.append(one_id)
                one_comment=json.loads(u_c_r.text)["data"]["data"][m]["text"]
                comment.append(one_comment)
        except:
            pass
    
    # 获取每个user对应的containerid
    user_base_url="https://m.weibo.cn/api/container/getIndex?type=uid&value="
    for id in set(user_id):#需要对user_id去重
        containerid_url=user_base_url+str(id)
        try:
            con_r=requests.get(containerid_url)
            one_containerid=json.loads(con_r.text)["data"]['tabsInfo']['tabs'][0]["containerid"]
            containerid.append(one_containerid)
        except:
            # by peter: 因为要与user_id对应zip
            containerid.append(0)
    
    # 获取每个user_id对应的基本信息
    # 这里需要设置cookie和headers模拟请求
    user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
    headers={"User-Agent":user_agent}
    m=1
    for num in zip(user_id,containerid):
        # by peter: num[0]user_id,num[1]containerid
        url = "https://m.weibo.cn/api/container/getIndex?uid="+str(num[0])+"&luicode=10000011&lfid=100103type%3D1%26q%3D&featurecode=20000320&type=uid&value="+str(num[0])+"&containerid="+str(num[1])
        try:
            # edit by peter: 去掉cookies=cookie
            r=requests.get(url,headers=headers)
            # edit by peter: 结构有变化,取数失败
            item_content=json.loads(r.text)["data"]["cards"][0]["card_group"][0]["item_content"].split("  ")
            feature.append(item_content)
            print("成功第{}条".format(m))
            logging.info(item_content)
            m+=1
            time.sleep(1)
        except:
            id_lose.append(num[0])
        
    
    # logging.info(id_lose)
    # 将featrue建立成DataFrame结构便于后续分析
    # edit by peter: 结构有变化,取数失败
    comment_info=pd.DataFrame(comment,columns=["评论"])
    comment_info.to_csv("comment_info.csv",index=False,encoding="gb18030")

    user_info=pd.DataFrame(feature,columns=["性别","年龄","星座","国家城市"])
    user_info.to_csv('user_info.csv',index=False,encoding='gb18030')
    logging.info("Save csv")