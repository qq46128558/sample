#!/usr/bin/env ptyhon3

'猫眼最受期待榜top50'

# http://maoyan.com/board/6?offset=0

import logging 
import requests
from bs4 import BeautifulSoup
import threading
import time


def get_one_page(url):
	headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
    }
	response=requests.get(url,headers=headers)
	if response.status_code==200:
		return response.text
	return None

'''<dd>
                        <i class="board-index board-index-11">11</i>
    <a href="/films/1229214" title="爸，我一定行的" class="image-link" data-act="boarditem-click" data-val="{movieId:1229214}">
      <img src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png" alt="" class="poster-default">
      <img alt="爸，我一定行的" class="board-img" src="http://p1.meituan.net/movie/808c13573707a7414224bb1a28fde34b853667.jpg@160w_220h_1e_1c">
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1229214" title="爸，我一定行的" data-act="boarditem-click" data-val="{movieId:1229214}">爸，我一定行的</a></p>
<p class="star">主演：郑润奇,郑鹏生,张咏娴</p><p class="releasetime">上映时间：2018-08-24</p>    </div>
    <div class="movie-item-number wish">
        <p class="month-wish">本月新增想看：<span><span class="stonefont"></span></span>人</p>
        <p class="total-wish">总想看：<span><span class="stonefont"></span></span>人</p>
    </div>

      </div>
    </div>

                </dd>'''
def parse_one_page(html):
	bsobj=BeautifulSoup(html,'html.parser')
	dl=bsobj.findAll("dd")
	for dd in dl:
		yield {
			'no':dd.i.get_text(),
			'title':dd.a['title'],
			'releasetime':dd.find('p',{'class':'releasetime'}).get_text()[5:],
			# 反爬虫字体,未研究
			# 'total-wish':dd.find('span',{'class':'stonefont'}).get_text(),
		}

def scraping(offset):
	global items
	baseurl="http://maoyan.com/board/6?offset={}"
	try:
		html=get_one_page(baseurl.format(offset))
		# iterator
		for item in parse_one_page(html):
			items.append(item)

	except Exception as e:
		logging.error(str(e))

# 列表排序用
def sortno(dict):
	return int(dict['no'])

if __name__=='__main__':
	logging.basicConfig(level=logging.INFO)
	items=[]

	# 多线程 0.327s
	start=time.time()
	threads=[]
	for i in range(5):
		threads.append(threading.Thread(target=scraping,name="T"+str(i),args=(i*10,)))
	for t in threads:
		t.start()
	for t in threads:
		t.join()
	items.sort(key=sortno)
	print(items)
	end=time.time()
	print('Scraping time:',round(end-start,3),'s') 

	# 单线程 1.037 s
	# start=time.time()
	# for i in range(5):
	# 	scraping(i*10)
	# items.sort(key=sortno)
	# print(items)
	# end=time.time()
	# print('Scraping time:',round(end-start,3),'s') 
