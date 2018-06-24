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
from bs4 import BeautifulSoup

# 画图
import matplotlib.pyplot as plt

# 截取词
import jieba
# 处理词
import pandas as pd
# 词频统计
import numpy
# 词云
from scipy.misc import imread
from wordcloud import WordCloud,ImageColorGenerator

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
    url='https://sou.zhaopin.com/jobs/searchresult.ashx?'
    try:
        # 获取网页内容，返回html数据
        response=requests.get(url,params=paras,headers=headers)
        # 通过状态码判断是否获取成功
        if response.status_code==200:
            return response.text
        return None
    except RequestException as e:
        return None

# 获取详细页面
def get_detail_page(url):
    # 此处host不同
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        'Host': 'jobs.zhaopin.com',
        'Referer': 'https://www.zhaopin.com/',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
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
    pattern = re.compile('<td class="zwmc".*?href="(.*?)" target="_blank">(.*?)</a>.*?'         # 匹配职位详情地址和职位名称
       '<td class="gsmc"><a href="(.*?)" target="_blank">(.*?)</a>.*?'                          # 匹配公司网址和公司名称
       '<td class="zwyx">(.*?)</td>.*?'                                                         # 匹配月薪      
       '<td class="gzdd">(.*?)</td>', re.S)                               
    # 匹配所有符合条件的内容
    items=re.findall(pattern,html)
    # ('网站开发工程师', 'http://company.zhaopin.com/CC276898035.htm', '珠海横琴天汇星实业有限公司', '4001-6000')
    for item in items:
        salary_avarage=0
        temp=item[4]
        if temp!='面议':
            idx=temp.find('-')
            # 求平均工资
            salary_avarage=(int(temp[0:idx])+int(temp[idx+1:]))//2
        job_name=item[1]
        job_name=job_name.replace('<b>','')
        job_name=job_name.replace('</b>','')
        yield{
            'job_url':item[0],
            '职位':job_name,
            '公司':item[3],
            '月薪':salary_avarage,
            '地点':item[5]
        }

# 获取职位明细信息       
def get_job_detail(html):
    requirement=''
    # 使用BeautifulSoup进行数据筛选
    soup=BeautifulSoup(html,'html.parser')
    # 找到<ul class="terminal-ul clearfix">标签
    for ul in soup.find_all('ul',class_='terminal-ul clearfix'):
        # 该标签共有8个子标签，分别为：
        # 职位月薪|工作地点|发布日期|工作性质|工作经验|最低学历|招聘人数|职位类别
        lis=ul.find_all('strong')
        # 工作经验
        years=lis[4].get_text()
        # 最低学历
        education=lis[5].get_text()
    # 筛选任职要求
    for terminalpage in soup.find_all('div',class_="terminalpage-main clearfix"):
        for box in terminalpage.find_all('div',class_='tab-cont-box'):
            cont=box.find_all('div',class_='tab-inner-cont')[0]
            ps=cont.find_all('p')
            # "立即申请"按钮也是个p标签，将其排除
            for i in range(len(ps)-1):
                requirement+=ps[i].get_text().replace("\n","").strip() # 去掉换行符和空格
    # 筛选公司规模，该标签内有四个或五个<li>标签，但是第一个就是公司规模
    scale=soup.find(class_="terminal-ul clearfix terminal-company mt20").find_all('li')[0].strong.get_text()
    return {'years':years,'education':education,'requirement':requirement,'scale':scale}


def write_csv_file(path,headers,rows):
    """ 将表头和行写入csv文件 """
    # 加入encoding防止中文写入报错
    # newline参数防止每写入一行都多一个空行
    with open(path,'a',encoding='gb18030',newline='') as f:
        f_csv=csv.DictWriter(f,headers)
        # f_csv=csv.writer(f)
        f_csv.writeheader()
        f_csv.writerows(rows)

# csv文件采用逐行写入的方式这样也可以省点内存
def write_csv_rows(path,headers,rows):
    with open(path,'a',encoding='gb18030',newline='') as f:
        f_csv=csv.DictWriter(f,headers)
        # 如果写入数据为字典，则写入一行，否则写入多行
        if type(rows)==type({}):
            f_csv.writerow(rows)
        else:
            f_csv.writerows(rows)
# 写入文本文件
def write_txt_file(path,txt):
    with open(path,'a',encoding='gb18030',newline='') as f:
        f.write(txt)

def write_csv_headers(path, headers):
    with open(path,'a',encoding='gb18030',newline='') as f:
        f_csv=csv.DictWriter(f,headers)
        f_csv.writeheader()

def main(city,keyword,region,pages):
    """ 主函数 """
    csv_filename='zl_'+city+'_'+keyword+'.csv'
    txt_filename='zl_'+city+'_'+keyword+'.txt'
    headers=['职位','经验','学历','公司','规模','月薪','地点']
    write_csv_headers(csv_filename, headers)

    for i in range(pages):
        # 获取该页中所有职位信息，写入csv文件
        job_dict={}
        html=get_one_page(city,keyword,region,i)
        items=parse_one_page(html)
        for item in items:
            html=get_detail_page(item.get('job_url'))
            job_detail=get_job_detail(html)
            job_dict['职位']=item.get('职位')
            job_dict['经验']=job_detail.get('years')
            job_dict['学历']=job_detail.get('education')
            job_dict['公司']=item.get('公司')
            job_dict['规模']=job_detail.get('scale')
            job_dict['月薪']=item.get('月薪')
            job_dict['地点']=item.get('地点')
            # 对数据进行清洗，将标点符号等对词频统计造成影响的因素剔除
            # [\u4E00-\u9FD5]中文字的unicode范围
            pattern = re.compile(r'[\u4E00-\u9FD5]+')
            filterdata = re.findall(pattern, job_detail.get('requirement'))
            # filterdata = job_detail.get('requirement')
            write_txt_file(txt_filename,''.join(filterdata))
            write_csv_rows(csv_filename,headers,job_dict)

    # 工资统计
    if True:
        salaries=[]
        sal=read_csv_column(csv_filename,5)
        # 撇除第一项，并转换成整形，生成新的列表

        for i in range(len(sal)-1):
            print(i)
            # 工资为'0'的表示招聘上写的是'面议',不做统计
            if not (sal[i]=='0' or sal[i]=='月薪'):
                salaries.append(int(sal[i]))
        # 用直方图进行展示
        # 注意生成文件后会报错：ValueError: invalid literal for int() with base 10: '月薪'
        plt.hist(salaries,bins=10,)
        plt.show()

    if True:
        # 职位描述词频统计
        content=read_txt_file(txt_filename)
        segment=jieba.lcut(content)

        words_df=pd.DataFrame({'segment':segment})
        # 忽略常用词
        stopwords=pd.read_csv("stopwords.txt",index_col=False,quoting=3,sep=" ",names=['stopword'],encoding='utf-8')
        words_df=words_df[~words_df.segment.isin(stopwords.stopword)]

        words_stat=words_df.groupby(by=['segment'])['segment'].agg({"计数":numpy.size})
        words_stat=words_stat.reset_index().sort_values(by=["计数"],ascending=False)

        # 设置词云属性
        color_mask = imread('china.jfif')
        wordcloud=WordCloud(font_path='simhei.ttf', # 设置字体可以显示中文
        background_color="white",                   # 背景颜色
        max_words=100,                              # 词云显示的最大词数
        mask=color_mask,                            # 设置背景图片
        max_font_size=100,                          # 字体最大值
        random_state=42,
        width=1000,height=860,margin=2,             # 设置图片默认的大小,但是如果使用背景图片的话那么保存的图片大小将会按照其大小保存,margin为词语边缘距离
        )
        # 生成词云, 可以用generate输入全部文本,也可以我们计算好词频后使用generate_from_frequencies函数
        word_frequence={x[0]:x[1] for x in words_stat.head(100).values}
        # {'经验': 34, '开发': 34, '网站': 29, ...
        word_frequence_dict={}
        for key in word_frequence:
            word_frequence_dict[key]=word_frequence[key]
        wordcloud.generate_from_frequencies(word_frequence_dict)
        # 从背景图片生成颜色值
        image_colors=ImageColorGenerator(color_mask)
        # 重新上色
        wordcloud.recolor(color_func=image_colors)
        # 保存图片
        wordcloud.to_file('output.jpg')
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.show()


# 读取csv的一列    
def read_csv_column(path,column):
    with open(path,'r',encoding='gb18030',newline='') as f:
        reader=csv.reader(f)
        return [row[column] for row in reader]

# 读取txt文本
def read_txt_file(path):
    with open(path,'r',encoding='gb18030',newline='') as f:
        return f.read()


if __name__=='__main__':
    # 3185保税区 3184高新区 3183横琴新区 3182金湾区 3181斗门区 3180香洲区 0不限
    city,keyword,region='珠海','PHP开发工程师',0
    # 获取职位个数
    html=get_one_page(city,keyword,region,1)
    pcount=parse_position_count(html)
    # 每页60个
    pages=math.ceil(pcount/60)
    main(city,keyword,region,pages)
    
""" 可以继续发挥：
分析工作年限和工资的关系并展示、预测
统计不同工作岗位的薪资差别
利用多线程或多进程提升效率 """