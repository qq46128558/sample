from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

pages=set()
def getLinks(pageUrl):
    global pages
    html=urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj=BeautifulSoup(html,'html.parser')
    for link in bsObj.findAll("a",href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 遇到了新页面
                newPage=link.attrs['href']
                print(newPage)
                pages.add(newPage)
                # python默认的递归限制是1000,达到递归限制就会停止,除非设置一个较大的递归计数器
                getLinks(newPage)

if __name__=='__main__':
    getLinks("")
