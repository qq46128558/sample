#!/usr/bin/env python3

'电影评论词云图'

import logging
import pandas as pd
import jieba
import pickle
from os import path
import matplotlib.pyplot as plt
# https://www.lfd.uci.edu/~gohlke/pythonlibs/ wordcloud下载
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator


logging.basicConfig(level=logging.ERROR)

df=pd.read_csv('hidden_man_norepeat.csv',encoding='gb18030')

comment=df['评论'].tolist()
# 查看里面字符串换行的编码:发现是/r/r/n
logging.info(comment[1].encode('gbk'))

# 替换掉换行
comment=list(map(lambda x:x.replace('\r\r\n',''),comment))

# 截词
comment_cut=jieba.cut(str(comment),cut_all=False)

# for i in range(6):
#     logging.info(next(comment_cut))
# INFO:root:[
# INFO:root:'
# Building prefix dict from the default dictionary ...
# DEBUG:jieba:Building prefix dict from the default dictionary ...
# Loading model from cache C:\Users\Peter\AppData\Local\Temp\jieba.cache
# DEBUG:jieba:Loading model from cache C:\Users\Peter\AppData\Local\Temp\jieba.cache
# Loading model cost 1.404 seconds.
# DEBUG:jieba:Loading model cost 1.404 seconds.
# Prefix dict has been built succesfully.
# DEBUG:jieba:Prefix dict has been built succesfully.
# INFO:root:完全
# INFO:root:不
# INFO:root:知道
# INFO:root:演

# 将词连接成字符串
word_space_split=" ".join(comment_cut)

# 导入背景图
background_image=plt.imread('./WeChat Image_20180727141117.jpg')
stopwords=STOPWORDS.copy()
# 可以加多个屏蔽词
for i in ["电影","姜文","彭于","真的","有点","廖凡","演技","演员","超级","但是","就是","剧情","一个","一部","看到","还是","不是","什么","感觉","这部","子弹","片子"]:
    stopwords.add(i)
# 设置词云参数 
# 参数分别是指定字体、背景颜色、最大的词的大小、使用给定图作为背景形状
wc = WordCloud(width=1024,height=768,background_color='white',mask=background_image,font_path = 'simhei.ttf',stopwords=stopwords,max_font_size=400,random_state=50)
# wc.generate_from_text("中国 中国 北京 珠海 珠海 珠海 深圳")
wc.generate_from_text(word_space_split)

# 从背景图中取色
img_colors= ImageColorGenerator(background_image)
wc.recolor(color_func=img_colors)

# 保存结果到本地
wc.to_file('hm.jpg')

plt.imshow(wc)
plt.axis('off') # 不显示坐标轴  
plt.show()

