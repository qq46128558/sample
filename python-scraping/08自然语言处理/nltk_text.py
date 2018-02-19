'自然语言工具包（Natural Language Toolkit，NLTK）'

'用 NLTK 做统计分析一般是从 Text 对象开始的'
from nltk import word_tokenize
from nltk import Text
#  NLTK 库里已经内置了几本书
from nltk.book import *

tokens=word_tokenize("Here is some not very interesting text")
text=Text(tokens)
