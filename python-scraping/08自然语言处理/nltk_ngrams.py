'自然语言工具包（Natural Language Toolkit，NLTK）'

from nltk import ngrams
from nltk.book import *
from nltk import FreqDist

# 查出“father smelt ofelderberries”这个短语在剧本中只出现了一次
fourgrams=ngrams(text6,4)
fourgramsDist=FreqDist(fourgrams)
fourgramsDist[("father","smelt","of","elderberries")]

# 打印文本中所有以“coconut”开头的 4-gram 序列
for fourgram in fourgrams:
    if fourgram[0]=="cocount":
        print(fourgrams)
