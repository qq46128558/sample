from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO

from bs4 import BeautifulSoup

# 这段代码把一个远程 Word 文档读成一个二进制文件对象（ BytesIO 与本章之前用的StringIO 类似），再用 Python 的标准库 zipfile 解压（所有的 .docx 文件为了节省空间都进行过压缩），然后读取这个解压文件，就变成 XML 了。
wordFile=urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
wordFile=BytesIO(wordFile)
document=ZipFile(wordFile)
xml_content=document.read('word/document.xml')
# print(xml_content.decode('utf-8'))

wordObj=BeautifulSoup(xml_content.decode('utf-8'),'xml')

# textString=wordObj.find("w:t")
# for textElem in textString:
#     # 没有text属性
#     # print(textElem.text)
#     print(textElem)

textString=wordObj.findAll("w:t")
for textElem in textString:
    # print(textElem.parent.previousSibling.find("w:pStyle"))
    closeTag=""
    try:
        # 文档的标题是由样式定义标签 <w:pStyle w:val="Title"/> 处理的。注意S大写
        style=textElem.parent.previousSibling.find("w:pStyle")
        if style is not None and style['w:val']=="Title":
            print("<h1>")
            closeTag="</h1>"
    except AttributeError:
        #不打印标签
        pass
    print(textElem)
    print(closeTag)
