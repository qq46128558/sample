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
            if link.attrs['href'] not in internalLinks:
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
    # print(splitAddress(startingPage)[0])
    # [0]取host name
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

# 收集网站上发现的所有外链列表
allExtLinks=set()
allIntLinks=set()
def getAllExternalLinks(siteUrl):
    html=urlopen(siteUrl)
    bsObj=BeautifulSoup(html,'html.parser')
    internalLinks=getInternalLinks(bsObj,splitAddress(siteUrl)[0])
    externalLinks=getExternalLinks(bsObj,splitAddress(siteUrl)[0])
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            print("即将获取链接的URL是:"+link)
            allIntLinks.add(link)
            getAllExternalLinks(link)


# 从互联网上不同的网站采集外链
# followExtenalOnly("http://oreilly.com")

# 收集内链和外链
getAllExternalLinks("http://oreilly.com")
