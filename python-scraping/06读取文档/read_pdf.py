from urllib.request import urlopen
from io import StringIO
from io import open
from pdfminer.pdfinterp import PDFResourceManager,process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

def readPDF(pdfFile):
    rsrcmgr=PDFResourceManager()
    retstr=StringIO()
    laparams=LAParams()
    device=TextConverter(rsrcmgr,retstr,laparams=laparams)

    process_pdf(rsrcmgr,device,pdfFile)
    device.close()

    content=retstr.getvalue()
    retstr.close()
    return content

pdfFile=urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
outputString=readPDF(pdfFile)
print(outputString)
pdfFile.close()

# 输出结果可能不是很完美，尤其是当 PDF 里有图片、各种各样的文本格式，或者带有表格和数据图的时候。但是，对大多数只包含纯文本内容的 PDF 而言，其输出结果与纯文本格式基本没什么区别。