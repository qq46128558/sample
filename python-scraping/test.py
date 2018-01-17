from bs4 import BeautifulSoup
from urllib.request import urlopen

try:
    html=urlopen("http://www.hanweb.com/module/download/downfile.jsp?filename=1411061517113078473.pdf")
    bsObj=BeautifulSoup(html)
except Exception as e:
    print(e)