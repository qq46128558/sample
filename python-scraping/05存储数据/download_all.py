# os 模块是Python 与操作系统进行交互的接口
import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory="download"
baseUrl="http://pythonscraping.com"


# 对 URL 链接进行清理和标准化，获得文件的绝对路径（而且去掉了外链）
def getAbsoluteUrl(baseUrl,source):
    if source.startswith("http://www."):
        url="http://"+source[11:]
    elif source.startswith("http://"):
        url=source
    elif source.startswith("www."):
        url=source[4:]
        url="http://"+source
    else:
        url=baseUrl+"/"+source
    if baseUrl not in url:
        return None
    print("url",url)
    return url


def getDownloadPath(baseUrl,absoluteUrl,downloadDirectory):
    path=absoluteUrl.replace("www.","")
    path=path.replace(baseUrl,"")
    path=downloadDirectory+path
    directory=os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)
    print("path",path)
    return path

html=urlopen("http://www.pythonscraping.com")
bsObj=BeautifulSoup(html,'html.parser')
# 首先使用 Lambda 函数（第 2 章介绍过）选择首页上所有带 src 属性的标签
downloadList=bsObj.findAll(src=True)

for download in downloadList:
    print("download['src']",download["src"])
    fileUrl=getAbsoluteUrl(baseUrl,download["src"])
    if fileUrl is not None:
        print("fileUrl",fileUrl)

# 下载到程序所在文件夹的 downloadDirectory 文件里
urlretrieve(fileUrl,getDownloadPath(baseUrl,fileUrl,downloadDirectory))

