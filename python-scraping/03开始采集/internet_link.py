from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages=set()
random.seed(datetime.datetime.now())

# 获取页面所有内链的列表
def getInternalLinks(bsObj,includeUrl):
    internalLinks=[]
    # 找出所有以/开头的链接
    for link in bsObj.findAll("a",href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if links.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

# 获取页面所有外链的列表
def getExternalLinks(bsObj,excludeUrl):
    externalLinks=[]
    # 找出所有以http或www开头且不包含当前url的链接
    for link in bsObj.findAll("a",href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts=address.replace("http://","").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html=urlopen(startingPage)
    bsObj=BeautifulSoup(html,'html.parser')
    externalLinks=getExternalLinks(bsObj,splitAddress(startingPage)[0])
    if len(externalLinks)==0:
        internalLinks=getInternalLinks(startingPage)
        # return getNextExternalLinks(internalLinks[random.randint(0,len(internalLinks)-1)])
        return None
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]

def followExtenalOnly(startingSite):
    externalLink=getRandomExternalLink(startingSite)
    if externalLink==None:
            exit()
    print("随机外链是:"+externalLink)
    followExtenalOnly(externalLink)

followExtenalOnly("http://oreilly.com")
