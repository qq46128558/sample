#!/usr/bin/env python3

'词云基本用法'

import logging
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
# 引入matplotlib处理图像
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)

# 词云背景图 用pyplot加载
background_image=plt.imread('./pic.jpg')
# 屏蔽词(可add)
stopwords=STOPWORDS.copy()
stopwords.add('的')
# 从背景图中取色
img_colors= ImageColorGenerator(background_image)

# 词云图初始化
wc = WordCloud(
    width=1024,height=768, # 生成的图尺寸,有mask时不生效
    background_color='white', # 背景色
    mask=background_image, # 词云轮廓
    font_path = 'simhei.ttf', # 使用的字体
    stopwords=stopwords, # 屏蔽词
    max_font_size=400, # 词频最高的字体大小
    random_state=50, # 未知
    max_words=100 # 最大词数
    )
mylist=['的 '*10]
mylist.append('蔚蓝路 '*5)
mylist.append('星云路 '*1)
mylist.append('粤海路 '*2)

word_text=" ".join(mylist)
# 不同频次,有时会重复,有时不重复,未知规律
wc.generate_from_text(word_text)
# 重新以背景图颜色上色
wc.recolor(color_func=img_colors)
# 保存结果到本地
wc.to_file('wordcloud.jpg')

logging.info(type(wc))

# 用pyplot显示词云图
plt.imshow(wc)
plt.axis('off')
plt.show()