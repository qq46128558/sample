'爬取大众点评城市的餐厅(小龙虾标签)信息'

import logging
from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup
import pandas as pd
import time

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

def get_city_info():
    """ 遇到问题，爬取到的soup与浏览器中看到的不同,目前只能查看str(soup)的结构再截取 """
    """ 还有滑动验证 """
    baseurl='http://www.dianping.com/{}/ch10/g219'.format('beijing')
    try:
        html=get_one_page(baseurl)
        soup=BeautifulSoup(html,'html.parser')
        # with open('soup.txt','w',encoding='utf-8') as f:
        #     f.write(str(soup))
        
        # 爬取总页数(上一页的前一个兄弟标签即为总页数)(前一个是空白)
        # tag=soup.find('a',class_='next').previous_sibling.previous_sibling
        # totalpage=int(tag.string) if tag!=None else 1
        # logging.debug(totalpage)
        totalpage=1
        for i in range(1,totalpage+1):
            if i!=1:
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
                logging.info(tags[j].div.a.h4.text) # 餐厅
                logging.info(tags[j].find('div',class_='comment').a.b.text) # 点评
                logging.info(tags[j].find('a',class_='mean-price').b.text if tags[j].find('a',class_='mean-price').b!=None else '-') #人均
                logging.info(tags_comment[j].find_all('span')[0].text)
                logging.info(tags_comment[j].find_all('span')[1].text)
                logging.info(tags_comment[j].find_all('span')[2].text)
    except Exception as e:
        logging.error(str(e))


if __name__=='__main__':
    start=time.time()
    get_city_info()
    # df=pd.DataFrame(data)
    # df.to_csv('city_info.csv',index=False,encoding='gb18030')
    end=time.time()
    print("Scraping time:%ds"%(round(end-start,3)))