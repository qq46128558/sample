'自然语言工具包（Natural Language Toolkit，NLTK）'

from nltk.book import *
from nltk import bigrams
from nltk import FreqDist

bigrams=bigrams(text6)
bigramsDist=FreqDist(bigrams)
bigramsDist[("Sir","Robin")]
