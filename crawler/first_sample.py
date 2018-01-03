# coding: UTF-8

'第一个python爬虫实例'

# 用来抓取网页的html源代码
import requests
# 将数据写入到csv文件中 
import csv
# 取随机数 
import random
# 时间相关操作
import time
# 在这里只用于异常处理
import socket
import http.client
# 用来代替正则式取源码中相应标签中的内容
from bs4 import BeautifulSoup
# 另一种抓取网页的html源代码的方法，但是没requests方便（我一开始用的是这一种）
# import urllib.request

# 获取网页中的html代码：
def get_content(url,data=None):
    # header是requests.get的一个参数，目的是模拟浏览器访问 
    # header 可以使用chrome的开发者工具获得
    header={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip,deflate,sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }
    # timeout是设定的一个超时时间，取随机数是因为防止被网站认定为网络爬虫
    timeout=random.choice(range(80,180)) # 80~179
    while True:
        try:
            rep=requests.get(url,headers=header,timeout=timeout)
            # rep.encoding = ‘utf-8’是将源代码的编码格式改为utf-8（不然源代码中中文部分会为乱码）
            rep.encoding='utf-8'
            # req = urllib.request.Request(url, data, header)
            # response = urllib.request.urlopen(req, timeout=timeout)
            # html1 = response.read().decode('UTF-8', errors='ignore')
            # response.close()
            break
        # except urllib.request.HTTPError as e:
        #         print( '1:', e)
        #         time.sleep(random.choice(range(5, 10)))
        #
        # except urllib.request.URLError as e:
        #     print( '2:', e)
        #     time.sleep(random.choice(range(5, 10)))
        # 下面是一些异常处理
        except socket.timeout as e:
            print('3:',e)
            time.sleep(random.choice(range(8,15)))
        except socket.error as e:
            print('4:',e)
            time.sleep(random.choice(range(20,60)))
        except http.client.BadStatusLine as e:
            print('5:',e)
            time.sleep(random.choice(range(30,80)))
        except http.client.IncompleteRead as e:
            print('6:',e)
            time.sleep(random.choice(range(5,15)))
    # 返回 rep.text
    return rep.text
    # return html_text

# 首先还是用开发者工具查看网页源码，并找到所需字段的相应位置
# 找到我们需要字段都在 id = “7d”的“div”的ul中。日期在每个li中h1 中，天气状况在每个li的第一个p标签内，最高温度和最低温度在每个li的span和i标签中。 
# 感谢Joey_Ko指出的错误：到了傍晚，当天气温会没有最高温度，所以要多加一个判断。 
def get_data(html_text):
    final=[]
    # 创建BeautifulSoup对象
    bs=BeautifulSoup(html_text,'html.parser')
    # 获取body部分
    body=bs.body
    # 找到id为7d的div
    data=body.find('div',{'id':'7d'})
    # 获取ul部分
    ul=data.find('ul')
    # 获取所有的li
    li=ul.find_all('li')

    # 对每个li标签中的内容进行遍历
    for day in li:
        temp=[]
        # 找到日期
        date=day.find('h1').string
        # 添加到temp中
        temp.append(date)
        # 找到li中的所有p标签
        inf=day.find_all('p')
        # 第一个p标签中的内容（天气状况）加到temp中
        temp.append(inf[0].string,)
        if inf[1].find('span') is None:
            # 天气预报可能没有当天的最高气温（到了傍晚，就是这样），需要加个判断语句,来输出最低气温
            temperature_highest=None
        else:
            # 找到最高温
            temperature_highest=inf[1].find('span').string
            # 到了晚上网站会变，最高温度后面也有个℃
            temperature_highest=temperature_highest.replace('℃','')
        # 找到最低温
        temperature_lowest=inf[1].find('i').string
        # 最低温度后面有个℃，去掉这个符号
        temperature_lowest=temperature_lowest.replace('℃','')
        # 将最高温添加到temp中
        temp.append(temperature_highest)
        # 将最低温添加到temp中
        temp.append(temperature_lowest)
        #将temp加到final中
        final.append(temp)
    return final

# 将数据抓取出来后我们要将他们写入文件，具体代码如下：
def write_data(data,name):
    file_name=name
    with open(file_name,'w',errors='ignore',newline='') as f:
        f_csv=csv.writer(f)
        f_csv.writerows(data)

if __name__=='__main__':
    url='http://www.weather.com.cn/weather/101190401.shtml'
    html=get_content(url)
    result=get_data(html)
    write_data(result,'weather.csv')

''' 总结一下，从网页上抓取内容大致分3步： 
1、模拟浏览器访问，获取html源代码 
2、通过正则匹配，获取指定标签中的内容 
3、将获取到的内容写到文件中 '''


