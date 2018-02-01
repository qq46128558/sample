from urllib.request import urlopen
# 英文
# textPage=urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt")
# 这段代码会把《战争与和平》原著（托尔斯泰用俄语和法语写的）的第 1 章打印到屏幕上。
textPage=urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")

# 乱码是因为 Python 默认把文本读成ASCII 编码格式，而浏览器把文本读成 ISO-8859-1 编码格式。其实都不对，应该用 UTF-8编码格式。
# print(textPage.read())

print(str(textPage.read(),'utf-8'))
# 这个页面不是 HTML，所以BeautifulSoup 库就没用了。一旦纯文本文件被读成字符串，你就只能用普通 Python 字符串的方法分析它了。
