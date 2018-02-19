'自然语言工具包（Natural Language Toolkit，NLTK）'

'这段代码只会打印包含单词“google”（或“Google”）作为名词而非动词的句子。当然，你也可以更明确地要求只打印标记是“NNP”（专用名词）的“Google”，但是 NLTK 有时也会判断错误，所以最好还是给自己留一些余地，具体情况由项目而定。'

from nltk import word_tokenize,sent_tokenize,pos_tag
sentences=sent_tokenize("Google is one of the best companies in the world. I constantly google myself to see what I'm up to.")
nouns=['NN','NNS','NNP','NNPS']

for sentence in sentences:
    if "google" in sentence.lower():
        taggedWords=pos_tag(word_tokenize(sentence))
        for word in taggedWords:
            if word[0].lower()=="google" and word[1] in nouns:
                print(sentence)
