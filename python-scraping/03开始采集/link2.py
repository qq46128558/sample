from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

pages=set()
def getLinks(pageUrl):
    global pages
    html=urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj=BeautifulSoup(html,'html.parser')
    try:
        print(bsObj.h1.get_text())
        # 第一段文字
        words=bsObj.find(id="mw-content-text").findAll("p")[0].get_text()
        # print(type(words))
        ''' UnicodeEncodeError: 'gbk' codec can't encode character u'\xa0' in position 错误
        如果在window下运行，原因： 
        对于Unicode字符，需要print出来的话，由于本地系统是Windows中的cmd，默认codepage是CP936，即GBK的编码，所以python解释器需要先将上述的Unicode字符编码为GBK，然后再在cmd中显示出来。但是由于该Unicode字符串中包含一些GBK中无法显示的字符，导致此时提示“’gbk’ codec can’t encode”的错误的。 '''
        print(words.encode('GBK','ignore'))
        # print(words.replace(u'\xa0', u' '))
        # 编辑链接只出现在词条页面上,li#ca-edit->span->a->href
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print('页面缺少一些属性,不过不用担心.')

    for link in bsObj.findAll("a",href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 遇到了新页面
                newPage=link.attrs['href']
                print("------------\n"+newPage)
                pages.add(newPage)
                # python默认的递归限制是1000,达到递归限制就会停止,除非设置一个较大的递归计数器
                getLinks(newPage)

if __name__=='__main__':
    getLinks("")
