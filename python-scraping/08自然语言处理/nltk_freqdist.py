'自然语言工具包（Natural Language Toolkit，NLTK）'

from nltk.book import *
from nltk import FreqDist

fdist=FreqDist(text6)
fdist.most_common(10)
fdist["Grail"]
