from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj=BeautifulSoup(html,'html.parser')
# BeautifulSoup允许把特定函数类型当作findAll函数的参数,唯一的限制条件是这些函数必须把一个标签作为参数且返回结果是布尔类型,BeautifulSoup用这个函数来评估它遇到的每个标签对象,把结果为真的保留
values=bsObj.findAll(lambda tag:len(tag.attrs)==2)
for x in values:
    print(x)
