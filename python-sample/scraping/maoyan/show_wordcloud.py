#!/usr/bin/env python3

'根据Code指定csv重新生成词云图'

import logging
# argparse处理运行时传递的命令行参数
import argparse
import pandas as pd
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator


logging.basicConfig(level=logging.INFO)
ap=argparse.ArgumentParser()
ap.add_argument("-c","--code",required=True,help="the maoyan film code",type=str,default="248566")
args=vars(ap.parse_args())
code=args["code"]
logging.info(code)

try:
	df=pd.read_csv('maoyan_'+code+'.csv',encoding='gb18030')

	comment=df['评论'].tolist()
	# comment=list(map(lambda x:x.replace('\r\r\n',''),comment))
	# iterator
	comment_cut=jieba.cut(str(comment),cut_all=False)
	word_space_split=" ".join(comment_cut)

	# background_image=plt.imread('./xxx.jpg')
	stopwords=STOPWORDS.copy()

	for i in ['电影']:
	    stopwords.add(i)

	# mask=background_image,
	wc = WordCloud(width=1024,height=768,background_color='white',font_path = 'simhei.ttf',stopwords=stopwords,max_font_size=400,random_state=50)
	wc.generate_from_text(word_space_split)

	# img_colors= ImageColorGenerator(background_image)
	# wc.recolor(color_func=img_colors)

	wc.to_file('maoyan_'+code+'.jpg')
	plt.imshow(wc)
	plt.axis('off')
	plt.show()
except Exception as e:
	logging.error(str(e))


