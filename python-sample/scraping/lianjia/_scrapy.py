#!/usr/bin/env python3

'北京链家租房数据'

import logging
import requests
import time
import re
# 解析网页，用xpath表达式与正则表达式一起来获取网页信息，相比bs4速度更快
from lxml import etree
import pandas as pd
# from urllib.request import urlopen
# from urllib.request import Request
# 引入多线程
import threading

def get_one_page(url):
    headers={"User-Agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}
    response=requests.get(url,headers=headers)
    # html=urlopen(Request(url,headers=headers))
    if response.status_code==200:
        return response.text
    return None

def get_areas(html):
    global dict
    content=etree.HTML(html)
    # @data-index属性
    areas=content.xpath("//dd[@data-index='0']//div[@class='option-list']/a/text()")
    areas_link=content.xpath("//dd[@data-index='0']//div[@class='option-list']/a/@href")
    logging.info(areas)
    threads=[]
    for i in range(1,len(areas)):
    # for i in range(1,2):
        threads.append(threading.Thread(target=get_areas_info,args=(areas[i],areas_link[i],),name="T"+str(i)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    df=pd.DataFrame(dict)   
    df.to_csv('lianjia.csv',index=False,encoding='utf_8_sig')

def get_areas_info(area,area_link):
    global dict
    if area_link[0]=="/":
        url = 'https://bj.lianjia.com' + area_link
    else:
        url=area_link
    html=get_one_page(url)
    totalpage=re.findall("page-data=\'{\"totalPage\":(\d+),\"curPage\"",html)
    logging.info(totalpage)
    totalpage=int(totalpage[0]) if totalpage!=[] else 0
    logging.info("{}区域有{}页".format(area,totalpage))
    
    for j in range(1,totalpage+1):
    # for j in range(1,2):
        time.sleep(1)
        html=get_one_page(url+"/pg{}".format(j))
        content=etree.HTML(html)
        length=len(content.xpath("//div[@class='where']/a/span/text()"))
        with lock:
            dict['area'].extend([area]*length)
            # 凯景铭座  
            dict["title"].extend(content.xpath("//div[@class='where']/a/span/text()"))
            # 4室1厅  
            dict["room_type"].extend(content.xpath("//div[@class='where']/span[1]/span/text()")) #if length==len(content.xpath("//div[@class='where']/span[1]/span/text()")) else ('page'+str(j))*length )
            # 178.91平米  
            dict["square"].extend(content.xpath("//div[@class='where']/span[2]/text()")) # if length==len(content.xpath("//div[@class='where']/span[2]/text()")) else ('page'+str(j))*length )
            # 东 南 北
            dict["position"].extend(content.xpath("//div[@class='where']/span[3]/text()")) # if length==len(content.xpath("//div[@class='where']/span[3]/text()")) else ('page'+str(j))*length )
            # 安定门租房
            dict["detail_place"].extend(content.xpath("//div[@class='other']/div/a/text()")) # if length==len(content.xpath("//div[@class='other']/div/a/text()")) else ('page'+str(j))*length )
            # 高楼层(共19层)
            dict["floor"].extend(content.xpath("//div[@class='other']/div/text()[1]")) # if length==len(content.xpath("//div[@class='other']/div/text()[1]")) else ('page'+str(j))*length )
            # 高楼层(共19层)
            dict["total_floor"].extend(content.xpath("//div[@class='other']/div/text()[1]")) # if length==len(content.xpath("//div[@class='other']/div/text()[1]")) else ('page'+str(j))*length )
            # 2001年建塔楼
            dict["house_year"].extend(content.xpath("//div[@class='other']/div/text()[2]")) # if length==len(content.xpath("//div[@class='other']/div/text()[2]")) else ('page'+str(j))*length )
            # 22000
            dict["price"].extend(content.xpath("//div[@class='col-3']/div/span/text()")) # if length==len(content.xpath("//div[@class='col-3']/div/span/text()")) else ('page'+str(j))*length )

        logging.info('{} 第{}页爬取完成'.format(area,j))
        # :['雅宝公寓\xa0\xa0', '保利蔷薇\xa0\xa0'
        # strlen=''
        # for key in dict:
        #     strlen+=key+":"+str(len(dict[key]))
        # logging.info(strlen)


def main():
    logging.basicConfig(level=logging.INFO)
    start=time.time()
    url="https://bj.lianjia.com/zufang"
    html=get_one_page(url)
    get_areas(html)
    end=time.time()
    print("Scraping time:%d minutes"%((end-start)//60))


lock=threading.Lock()
dict={'area':[],'title':[],'room_type':[],'square':[],'position':[],'detail_place':[],'floor':[],'total_floor':[],'house_year':[],'price':[]}

if __name__=='__main__':
    main()