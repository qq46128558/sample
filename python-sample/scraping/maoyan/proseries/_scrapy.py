#!/usr/bin/env python3

'猫眼APP提供了每日各大视频网站的播放量'

# 通过Fiddler分析得到数据接口地址, 以优酷网8月11号电视剧播放量为例： http://box.maoyan.com/proseries/api/seriesTopRank.json?platformType=1&seriesType=0&dateRange=0&date=2018-08-11
# 其中platformType=1表示平台为优酷，SeriesType=0表示类型为电视剧，dateRange=0表示为数据日榜，最后的date则为具体日期

import logging
import time
import pandas as pd
import json
import requests

def get_one_page(url):
	# cookie=r"__cfduid=db5a1be9d935ee1989f0c45d87b3ac49a1535435081; __utma=172570402.1049390859.1535435080.1535435080.1535435080.1; __utmc=172570402; __utmz=172570402.1535435080.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic"
	header={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
	try:
		# cookies=cookie,报错:string indices must be integers
		html=requests.get(url=url,headers=header)
		logging.debug(html)
		logging.debug(url)
		if html.status_code==200:
			return html.content
		else:
			return None
	except Exception as e:
		# string indices must be integers
		logging.error("Url:%s Exception:%s"%(url,str(e)))
		return None

def parser_one_page(html,type,platform):
	global play_data
	data=json.loads(html.decode('utf-8'))['data']['seriesDailyRankList']
	for item in data:
		play_data = play_data.append({'date':str(date)[0:10],
	                                  'name':item['name'],
	                                  'play_num':float(item['playCountDesc']),
	                                  'type':type,
	                                  'platform':platform,
	                                  'monopoly':item['platformInfoDescV2']},
	                                 ignore_index=True)

play_data=pd.DataFrame(columns=['date','name','play_num','type','platform','monopoly'])

if __name__=='__main__':
	start=time.time()
	logging.basicConfig(level=logging.INFO)
	baseurl= 'http://box.maoyan.com/proseries/api/seriesTopRank.json?platformType={}&seriesType={}&dateRange=0&date={}'
	dictType={0:'电视剧',1:'网络剧',2:'综艺'}
	dictPlatform={0:'优酷',1:'爱奇艺',2:'腾讯',3:'乐视',4:'搜狐',5:'PP',6:'芒果'}
	# 0电视剧,1网络剧,2综艺
	for i in range(0,3):
		# 播放平台 0优酷1爱奇艺2腾讯3乐视4搜狐5PP6芒果
		for j in range(0,7):
			# 日期
			for date in pd.date_range('2018-01-01','2018-08-28',freq='D'):
				try:
					time.sleep(0.5)
					html=get_one_page(baseurl.format(str(j),str(i),str(date)[0:10]))
					if html!=None:
						parser_one_page(html,dictType.get(i),dictPlatform.get(j))
				except Exception as e:
					logging.error(str(e))
			logging.info("{}{} 区间数据爬取完成".format(dictPlatform.get(j),dictType.get(i)))
	play_data.to_csv('proseries.csv',index=False,encoding='gb18030')
	end=time.time()
	print("Scraping time: %d minutes"%round((end-start)//60,0))
