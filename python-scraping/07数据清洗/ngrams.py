from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def ngrams(input,n):
    input=input.split(' ')
    output=[]
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output

html=urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj=BeautifulSoup(html,'html.parser')
content=bsObj.find("div",{"id":"mw-content-text"}).get_text()
# 首先用一些正则表达式来移除转义字符（ \n ），再把 Unicode 字符过滤掉
content=re.sub('\n+'," ",content)
content=re.sub(' +'," ",content)
content=bytes(content,"UTF-8")
content=content.decode("ascii","ignore")
# print(content)
ngrams=ngrams(content,2)
print(ngrams)
print("2-grams count is: "+str(len(ngrams)))
