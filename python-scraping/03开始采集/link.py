from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html=urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj=BeautifulSoup(html,'html.parser')
# with open("./href.txt",'w') as f:
#     for link in bsObj.findAll('a'):
#         if 'href' in link.attrs:
#             f.write(link['href'])

# 分析词条键接与其他键接的差异,调整代码
# id在bodyContent的div标签内
# url链接不包含冒号
# url链接都以/wiki/开头
for link in bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])
