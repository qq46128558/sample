from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj=BeautifulSoup(html,'html.parser')
# 兄弟标签
# 如果想让爬虫更稳定,最好还是让标签的选择更加具体,如果有属性,就利用标签的属性
for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
    # 打印产品列表里的所有行的产品,第一行表格标题除外
    print(sibling)
    
# previous_siblings 前面的兄弟标签
# next_sibling previous_sibling 兄弟标签一组
