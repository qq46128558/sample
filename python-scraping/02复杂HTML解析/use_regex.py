from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html=urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj=BeautifulSoup(html,'html.parser')
images=bsObj.findAll('img',{"src":re.compile("\.\./img/gifts/img.*\.jpg")})
# bs4.element.ResultSet 结果集
print(type(images))
for x in images:
    print(x['src'])
    # bs4.element.Tag 标签对象
    print(type(x))
    # 标签对象 获取它的全部属性
    print(x.attrs)
    # print(x.attrs['src'])
