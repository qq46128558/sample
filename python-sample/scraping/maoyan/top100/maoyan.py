
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'50 行代码教你爬取猫眼电影 TOP100 榜所有信息'

# 无论大型还是小型爬虫都不会脱离这三个模块
# HTML下载器、HTML解析器、数据存储器

__author__='丁彦军'

import requests
import re
from multiprocessing import Pool
import json

from requests.exceptions import RequestException

headers={'User-Agent':'Mozilla/5.0'}

# 构造html下载器
def get_one_page(url):
	try:
		res=requests.get(url,headers=headers)
		if res.status_code==200:
			return res.text
		return None
	except RequestException:
		return None

# 构造html解析器
def parse_one_page(html):
	# (.*?)提取值
	pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
		+'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
		+'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
	# re.findall(pattern,string[,flags])：搜索整个string，以列表的形式返回能匹配的全部子串，其中参数是匹配模式，如re.S表示点任意匹配模式，改变“.”的行为
	items=re.findall(pattern,html)
	for item in items:
    	# 用yield，函数返回的就是一个生成器，而生成器作为一种特殊的迭代器，可以用for——in方法，一次一次的把yield拿出来
		# yield item
		# ('99', 'http://p1.meituan.net/movie/a1634f4e49c8517ae0a3e4adcac6b0dc43994.jpg@160w_220h_1e_1c', '迁徙的鸟', '\n                主演：雅克·贝汉,Philippe Labro\n        ', '上映时间：2001-12-12(法国)', '9.', '1')
		yield {'index':item[0],
		# 'image':item[1],
		'title':item[2],
		# 'actor':item[3].strip()[3:],
		'time':item[4].strip()[5:],
		'score':item[5]+item[6]}

# 构造数据存储器
def write_to_file(content):
	# 要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码
    with open ('result.txt', 'a',encoding='utf-8') as f:
    	# json默认是以ASCII来解析code的，由于中文不在ASCII编码当中，因此就不让默认ASCII生效
        f.write(json.dumps(content,ensure_ascii=False) + '\n')
        f.close()

# 构造主函数，初始化各个模块
def main(offset):
	url='http://maoyan.com/board/4?offset=' + str(offset)
	html=get_one_page(url)
	for item in parse_one_page(html):
		print(item)
		# write_to_file(item)

if __name__=='__main__':
	# 为了提高速度，我们引入Pool模块，用多线程并发抓取
	p=Pool()
	p.map(main,[i*10 for i in range(10)])