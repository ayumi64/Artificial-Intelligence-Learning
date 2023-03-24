"""
# NLTK 是构建Python程序以处理自然语言的库。它为50多个语料库和词汇资源(如 WordNet )提供了易于使用的接口，以及一套用于分类、分词、词干、标记、解析和语义推理的文本处理库、工业级自然语言处理 (Natural Language Processing, NLP) 库的包装器。

# NLTK被称为 “a wonderful tool for teaching, and working in, computational linguistics using Python”。

"""


import nltk
from nltk.corpus import treebank

# 首次使用需要下载
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('treebank')

sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""
# Tokenize
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)

# Identify named entities
entities = nltk.chunk.ne_chunk(tagged)

# Display a parse tree
t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()
