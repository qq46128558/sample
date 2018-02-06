from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import OrderedDict

def cleanInput(input):
    # 首先用一些正则表达式来移除转义字符（ \n ），再把 Unicode 字符过滤掉
    # 这里首先把内容中的换行符（或者多个换行符）替换成空格
    input=re.sub('\n+'," ",input)
    # 剔除维基百科的引用标记（方括号包裹的数字，如 [1]）
    input=re.sub('\[[0-9]*\]',"",input)
    # 把连续的多个空格替换成一个空格，确保所有单词之间只有一个空格
    input=re.sub(' +'," ",input)
    # 把内容转换成 UTF-8 格式以消除转义字符
    input=bytes(input,"UTF-8")
    input=input.decode("ascii","ignore")
    cleanInput=[]
    input=input.split(' ')
    for item in input:
        # 这里用 import string 和 string.punctuation 来获取 Python 所有的标点符号
        # strip移动字符串头尾标点符号,连字符的单词（连字符在单词内部）仍然会保留
        item=item.strip(string.punctuation)
        # >>> import string
        # >>> print(string.punctuation)
        # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        if len(item)>1 or (item.lower()=='a' or item.lower()=='i'):
            cleanInput.append(item)
    return cleanInput

def ngrams(input,n):
    # 用正则清洗数据
    input=cleanInput(input)
    output=dict() 
    for i in range(len(input)-n+1):
        newNGram=" ".join(input[i:i+n])
        if newNGram in output:
            output[newNGram]+=1
        else:
            output[newNGram]=1
        # output.append(input[i:i+n])
    return output


html=urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj=BeautifulSoup(html,'html.parser')
content=bsObj.find("div",{"id":"mw-content-text"}).get_text()
ngrams=ngrams(content,2)
ngrams=OrderedDict(sorted(ngrams.items(),key=lambda t:t[1],reverse=True))
print(ngrams)
# print(ngrams["Python Software"])
print("2-grams count is: "+str(len(ngrams)))
