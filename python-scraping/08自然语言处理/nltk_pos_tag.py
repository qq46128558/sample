
'自然语言工具包（Natural Language Toolkit，NLTK）'

'Penn Treebank 语义标记'
''' CC 并列连接词（Coordinating conjunction）
CD 基数（Cardinal number）
DT 限定词（Determiner）
EX 表示存在性的“there”（Existential “there”）
FW 外来语（Foreign word）
IN 介词，从属连词（Preposition, subordinating conjunction）
JJ 形容词（Adjective）
JJR 形容词，比较级（Adjective, comparative）
JJS 形容词，最高级（Adjective, superlative）
LS 列表项标记符（List item marker）
MD 情态动词（Modal）
NN 名词，单数或不可数（Noun, singular or mass）
NNS 名词，复数（Noun, plural）
NNP 专有名词，单数（Proper noun, singular）
NNPS 专有名词，复数（Proper noun, plural）
PDT 前置限定词（Predeterminer）
POS 名词所有格 s 结尾（Possessive ending）
PRP 人称代词（Personal pronoun）
PRP$ 物主代词（Possessive pronoun）
RB 副词（Adverb）
RBR 副词，比较级（Adverb, comparative）
RBS 副词，最高级（Adverb, superlative）
RP 小品词（Particle）
SYM 符号（Symbol）
TO 介词“to”（“to”）
UH 感叹词（Interjection）
VB 动词，一般形式（Verb, base form）
VBD 动词，过去时（Verb, past tense）
VBG 动词，动名词或现在分词（Verb, gerund or present participle）
VBN 动词，过去分词（Verb, past participle）
VBP 动词，非第三人称单数（Verb, non-third person singular present）
VBZ 动词，第三人称单数（Verb, third person singular present）
WDT Wh- 限定词（Wh-determiner）
WP Wh- 代词（Wh-pronoun）
WP$ Wh- 物主代词（Possessive wh-pronoun）
WRB Wh- 副词（Wh-adverb） '''

''' NLTK 还可以用它的超级大字典分析文本内容，帮助人们寻找单词的含义。
NLTK 的一个基本功能是识别句子中各个词的词性 '''

from nltk.book import *
from nltk import word_tokenize
text=word_tokenize("Strange women lying in ponds distributing swords is no basis for a system of government. Supreme executive power derives from a mandate from the masses, not from some farcical aquatic ceremony.")
from nltk import pos_tag

pos_tag(text)
NLTK
# 可以基于句子的内容正确地识别出对应的用法。