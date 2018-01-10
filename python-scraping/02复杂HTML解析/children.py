from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError


def getChilds(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    try:
        childs=[]
        bsObj=BeautifulSoup(html,'html.parser')
        for child in bsObj.find("table",{"id":"giftList"}).children:
            childs.append(child)
    except AttributeError as e:
        return None
    return childs

if __name__=='__main__':
    print(getChilds("http://www.pythonscraping.com/pages/page3.html"))

# .children 子标签
# descendants 后代标签