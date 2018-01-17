from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

# 用系统当前时间生成一个随机数生成器,这样可以保证每次程序运行时,都是全新的随机数
random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html=urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj=BeautifulSoup(html,'html.parser')
    # with open("./href.txt",'w') as f:
    #     for link in bsObj.findAll('a'):
    #         if 'href' in link.attrs:
    #             f.write(link['href'])

    # 正则,?!,不包含.表示字符不能出现在目标字符串里.如果要在整个字符串中全部排除某个字符,就加上^和$符号
    ''' ^((?![A-Z]).)*$ 不包含大写字母 '''
    # 分析词条键接与其他键接的差异,调整代码
    # id在bodyContent的div标签内
    # url链接不包含冒号
    # url链接都以/wiki/开头
    # for link in bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
    #     if 'href' in link.attrs:
    #         print(link.attrs['href'])
    return bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))

links=getLinks("/wiki/Kevin_Bacon")
while len(links)>0:
    # random.randint()的函数原型为：random.randint(a, b)，用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b
    newArticle=links[random.randint(0,len(links)-1)].attrs["href"]
    print(newArticle)
    links=getLinks(newArticle)

# 维基百科六度分隔理论
