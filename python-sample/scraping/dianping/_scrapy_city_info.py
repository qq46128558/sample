'爬取大众点评城市的餐厅(小龙虾标签)信息'

import logging
from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup
import pandas as pd
import time
import threading
import random

logging.basicConfig(level=logging.INFO)

def get_one_page(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Accept-Language': 'zh,zh-CN;q=0.9',
    # 'Cache-Control': 'max-age=0',
    # 'Connection': 'keep-alive',
    # 'Host': 'www.dianping.com',
    # 'Upgrade-Insecure-Requests': '1',
    }
    html=urlopen(Request(url,headers=headers))
    html=html.read()
    return html

def get_city_info(df):
    """ 遇到问题，爬取到的soup与浏览器中看到的不同,目前只能查看str(soup)的结构再截取 """
    """ 还有滑动验证 """
    baseurl='http://www.dianping.com/{}/ch10/g219'
    dict={}
    for i in range(0,df['城市'].count()):
        error_i=i
        dict['城市']=df['城市'][i]
        try:
            html=get_one_page(baseurl.format(df.get('拼音')[i]))
            soup=BeautifulSoup(html,'html.parser')
            # with open('soup.txt','w',encoding='utf-8') as f:
            #     f.write(str(soup))
            
            # 爬取总页数(上一页的前一个兄弟标签即为总页数)(前一个是空白)
            pagetag=soup.find('a',class_='next')
            if pagetag==None:
                with lock:
                    items.append((dict['城市'],'没有',0,0,0,0,0))
                # 没有小龙虾餐厅下一个城市
                logging.info("%s没有小龙虾标记的餐厅."%(dict['城市']))
                continue
            tag=pagetag.previous_sibling.previous_sibling
            totalpage=int(tag.string) if tag!=None else 1
            logging.debug(totalpage)
            # totalpage=1
            for i in range(1,totalpage+1):
                if i!=1:
                    time.sleep(random.choice(range(30)))
                    html=get_one_page(baseurl+"p%d"%i)
                    soup=BeautifulSoup(html,'html.parser')
                # 爬取餐厅信息
                tags=soup.find_all('div',class_='txt')
                tags_comment=soup.find_all('span',class_='comment-list')
                for j in range(len(tags)):
                    # INFO:root:犟虾
                    # INFO:root:698
                    # INFO:root:￥125
                    # INFO:root:口味9.1
                    # INFO:root:环境9.0
                    # INFO:root:服务9.1
                    # logging.info(tags[j].div.a.h4.text) # 餐厅
                    # logging.info(tags[j].find('div',class_='comment').a.b.text) # 点评
                    # logging.info(tags[j].find('a',class_='mean-price').b.text if tags[j].find('a',class_='mean-price').b!=None else '-') #人均
                    # logging.info(tags_comment[j].find_all('span')[0].text)
                    # logging.info(tags_comment[j].find_all('span')[1].text)
                    # logging.info(tags_comment[j].find_all('span')[2].text)
                    dict['餐厅']=tags[j].div.a.h4.text
                    dict['点评']=int(tags[j].find('div',class_='comment').a.b.text) if tags[j].find('div',class_='comment').a.b!=None else 0
                    dict['人均']=tags[j].find('a',class_='mean-price').b.text if tags[j].find('a',class_='mean-price').b!=None else '￥0'
                    dict['人均']= dict['人均'][1:]
                    if (dict['点评']==0 or j>=len(tags_comment)):
                        dict['口味']=0
                        dict['环境']=0
                        dict['服务']=0
                    else:
                        dict['口味']=tags_comment[j].find_all('span')[0].b.text 
                        dict['环境']=tags_comment[j].find_all('span')[1].b.text
                        dict['服务']=tags_comment[j].find_all('span')[2].b.text
                    logging.info(dict)
                    with lock:
                        items.append((dict['城市'],dict['餐厅'],dict['点评'],dict['人均'],dict['口味'],dict['环境'],dict['服务']))
            logging.info("{}小龙虾餐厅数据爬取完成.".format(dict['城市']))
        except Exception as e:
            error_msg="%s/%s:%s"%(df.get('城市')[error_i],df.get('拼音')[error_i],str(e))
            logging.error(error_msg)
            with open('error.log','a',encoding='utf-8',errors='ignore') as f:
                f.write(error_msg+"\n")

items=[]
lock=threading.Lock()
if __name__=='__main__':
    start=time.time()
    df=pd.read_csv('city.csv',encoding='gb18030')
    threads=[]
    for x,y in [(0,800),(800,1600),(1600,df.get('城市').count())]:
        threads.append(threading.Thread(target=get_city_info,name='T'+str(x),args=(df.iloc[x:y].reset_index(drop=True),)))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    df=pd.DataFrame(data=items,columns={})
    df.to_csv('xiaolongxia.csv',index=False,encoding='gb18030')

    end=time.time()
    # print("Scraping time:%ds"%(round(end-start,3)))
    print('Scraping time:{} minutes'.format((end-start)//60))