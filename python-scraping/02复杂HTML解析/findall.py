from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

def getNameList(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    try:
        nl=[]
        bsObj=BeautifulSoup(html,"html.parser")
        # 可以获取页面中所有指定的标签
        nameList=bsObj.findAll("span",{"class":"green"})
        for name in nameList:
            # 把正在处理的html文档中所有的标签都清除,返回一个只包含文字的字符串
            nl.append(name.get_text())
    except AttributeError as e:
        return None
    return nl

if __name__=='__main__':
    print(getNameList("http://www.pythonscraping.com/pages/warandpeace.html"))

# .findAll({"h1","h2"})
# .findAll("span",{"class":{"green","red"}})
# BeautifulSoup定义
# findAll(tag,attributes,recursive,text,limit,keywords)
# find(tag,attributes,recursive,text,keywords)
# 递归参数recursive,默认true,设为false就只查文档的一级标签
# text,用标签的文本内容去匹配,而不是标签的属性
# .findAll(text="the prince")
# limit,范围限制参数,find其实等价于findAll的limit等于1
# keyword,选择具有指定属性的标签 .findAll(id="text") 同:.findAll("",{"id":"text"})

