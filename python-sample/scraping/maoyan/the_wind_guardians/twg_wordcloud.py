#!/usr/bin/env python3

'词云图'

import logging
import pandas as pd
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator


logging.basicConfig(level=logging.INFO)

df=pd.read_csv('the_wind_guardians_norepeat.csv',encoding='gb18030')

comment=df['评论'].tolist()
comment=list(map(lambda x:x.replace('\r\r\n',''),comment))
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

wc.to_file('twg.jpg')

plt.imshow(wc)
plt.axis('off')
plt.show()
