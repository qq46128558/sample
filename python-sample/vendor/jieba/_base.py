#!/usr/bin/env python3

'jieba分词模块'

import logging
import jieba

logging.basicConfig(level=logging.INFO)

mylist=[]
mylist.append('先帝创业未半而中道崩殂，今天下三分，益州疲弊，此诚危急存亡之秋也。然侍卫之臣不懈于内，忠志之士忘身于外者，盖追先帝之殊遇，欲报之于陛下也。诚宜开张圣听，以光先帝遗德，恢弘志士之气，不宜妄自菲薄，引喻失义，以塞忠谏之路也。')
mylist.append('宫中府中，俱为一体，陟罚臧否，不宜异同。若有作奸犯科及为忠善者，宜付有司论其刑赏，以昭陛下平明之理，不宜偏私，使内外异法也。')


cut_generator=jieba.cut(str(mylist),cut_all=False)
logging.info(type(cut_generator))
# INFO:root:<class 'generator'>


for x in cut_generator:
    logging.info(x)
# INFO:root:[
# INFO:root:'
# Building prefix dict from the default dictionary ...
# DEBUG:jieba:Building prefix dict from the default dictionary ...
# Loading model from cache C:\Users\Peter\AppData\Local\Temp\jieba.cache
# DEBUG:jieba:Loading model from cache C:\Users\Peter\AppData\Local\Temp\jieba.cache
# Loading model cost 1.260 seconds.
# DEBUG:jieba:Loading model cost 1.260 seconds.
# Prefix dict has been built succesfully.
# DEBUG:jieba:Prefix dict has been built succesfully.
# INFO:root:先帝
# INFO:root:创业
# INFO:root:未半而
# INFO:root:中道
# INFO:root:崩
# INFO:root:殂
# INFO:root:，
# INFO:root:今天
