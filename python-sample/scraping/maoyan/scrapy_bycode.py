#!/usr/bin/env python3

'根据code抓取猫眼电影评论信息'

import logging
# argparse处理运行时传递的命令行参数
import argparse
import pandas as pd
import requests
import json
import time
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator

# 引入进程池,多线程处理
from multiprocessing import Pool,freeze_support,RLock
import os

import threading

def get_one_page(url):
	headers={
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
	}
	response=requests.get(url,headers=headers)
	if response.status_code==200:
		return response.text
	raise Exception("response code:"+str(response.status_code)+ ", scraping page: None")

def parse_one_page(html):
	try:
		data=json.loads(html)['cmts']
		for item in data:
			yield {
                'comment':item['content'],
                'date':item['time'].split(' ')[0],
                'rate':item['score'],
                'city':item['cityName'],
                'nickname':item['nickName'],
            }
	except Exception as e:
		# logging.error(str(e))
		# return 	{
  #               'comment':'',
  #               'date':'',
  #               'rate':'',
  #               'city':'',
  #               'nickname':'',
  #           }
  		raise Exception(str(e))

def save_to_csv(items):
	df=pd.DataFrame(data=items,columns=['评论','日期','评分','城市','昵称'])
	# 数据去重
	df.drop_duplicates(subset=['评论','昵称'],keep='first',inplace=True)
	# 数据筛选
	df['评论']=df['评论'].str.replace('\r\r\n','')
	# 保存csv
	df.to_csv('maoyan_'+code+".csv",index=False,encoding='gb18030')

	comment_list=df['评论'].tolist()
	# comment_list=list(map(lambda x:x.replace('\r\r\n',''),comment_list))
	# 截词 iterator
	comment_cut=jieba.cut(str(comment_list),cut_all=False)
	word_space_split=" ".join(comment_cut)
	# 生成词云
	to_wordcloud(word_space_split)

# 单线程
def scraping():
	baseurl="http://m.maoyan.com/mmdb/comments/movie/"+code+".json?_v_=yes&offset={}"
	logging.info(baseurl)

	try:
		items=[]
		# 猫眼最多1000页，此处只爬100页
		for i in range(1,101):
			logging.info("Scraping page {}".format(i))
			# print("Scraping page {}".format(i))
			html=get_one_page(baseurl.format(i))
			if (html==None):
				raise Exception("Scraping nothing")
			for item in parse_one_page(html):
				items.append(list(item.values()))
			if i<100:
				time.sleep(1)
		save_to_csv(items)
	except Exception as e:
		logging.error(str(e))

# 多线程
def multi_scraping(page):
	# global items
	in_items=[]
	# logging.basicConfig(level=logging.INFO)
	baseurl="http://m.maoyan.com/mmdb/comments/movie/"+code+".json?_v_=yes&offset={}"
	logging.info(baseurl)
	try:
		logging.info("Scraping page {}".format(page))
		html=get_one_page(baseurl.format(page))
		if (html==None):
			raise Exception("Scraping nothing")
		for item in parse_one_page(html):
			# 无法返回global items,改为写csv文件
			in_items.append(list(item.values()))
		# print(in_items)
		df=pd.DataFrame(data=in_items)
		# 多线程这样写文件，有时出现合并的乱码
		df.to_csv('temp.csv',encoding='gb18030',mode='a')

		time.sleep(1)
	except Exception as e:
		logging.error(str(e))

# 多线程
def run_thread(status):
	global items
	baseurl="http://m.maoyan.com/mmdb/comments/movie/"+code+".json?_v_=yes&offset={}"
	logging.info(baseurl)
	# 爬取100页
	for page in [i*2-status for i in range(1,3)]:
		try:
			logging.info("Scraping page {}".format(page))
			html=get_one_page(baseurl.format(page))
			if (html==None):
				raise Exception("Scraping nothing")
			lock.acquire()
			for item in parse_one_page(html):
				# 多线程此处顺序会不定?
				items.append(list(item.values()))
		except Exception as e:
			logging.error(str(e))
		finally:
			lock.release()
			# 防止网站拉黑
			time.sleep(1)


def to_wordcloud(text):
	# background_image=plt.imread('./xxx.jpg')
	stopwords=STOPWORDS.copy()
	for i in ['电影','电影院','影片','IMAX']:
	    stopwords.add(i)
	# mask=background_image,
	wc = WordCloud(width=1024,height=768,background_color='white',font_path = 'simhei.ttf',stopwords=stopwords,max_font_size=400,random_state=50)
	wc.generate_from_text(text)

	# img_colors= ImageColorGenerator(background_image)
	# wc.recolor(color_func=img_colors)

	wc.to_file('maoyan_'+code+'.jpg')

	plt.imshow(wc)
	plt.axis('off')
	plt.show()

# 读多线程生成的临时csv
def read_from_csv():
	df=pd.read_csv('temp.csv',encoding='gb18030')
	# 数据去重
	df.drop_duplicates(subset=['0','4'],keep='first',inplace=True)
	# 删除多出来的无标题的行
	df.drop(df[df['0']=='0'].index,inplace=True)
	# 数据筛选
	df['0']=df['0'].str.replace('\r\r\n','')
	# 保存csv
	df.to_csv('maoyan_'+code+".csv",index=False,encoding='gb18030')
	# 删除临时文件
	os.remove('temp.csv')

	comment_list=df['0'].tolist()
	comment_cut=jieba.cut(str(comment_list),cut_all=False)
	word_space_split=" ".join(comment_cut)
	to_wordcloud(word_space_split)

# 全局变量，始终无法在多线程中用？
items=[]

logging.basicConfig(level=logging.INFO)
ap=argparse.ArgumentParser()
ap.add_argument("-c","--code",required=True,help="the maoyan film code",type=str,default="248566")
args=vars(ap.parse_args())
code=args["code"]

lock=threading.Lock()

if __name__=='__main__':
	logging.info(code)
	# scraping()
	
	# 多线程抓取(忽然无效果，未知)
	# freeze_support() # for windows support
	# # p=Pool(4,initargs=(RLock(),))
	# p=Pool(4)
	# for i in range(1, 2):
	# 	p.apply_async(multi_scraping,args=(i))
	# p.close()
	# p.join()
	# print(items)
	# # save_to_csv(items)

	# 多线程处理2,成功但效果不理想
	# p=Pool(4)
	# p.map(multi_scraping,[i for i in range(1,101)])
	# read_from_csv()

	# 多线程处理3(用两个线程,效果应该算是正常了)(毕竟python没有真正的多线程,因为GIL锁)
	start_time=time.time()
	t1=threading.Thread(target=run_thread,args=(0,))
	t2=threading.Thread(target=run_thread,args=(1,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	end_time=time.time()
	print('Scraping use %d seconds'%(end_time-start_time))
	save_to_csv(items)