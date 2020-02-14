#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rakutenma import RakutenMA

# Initialize a RakutenMA instance with an empty model
# the default ja feature set is set already
rma = RakutenMA(phi=1024, c=0.007812)  # Specify hyperparameter for SCW (for demonstration purpose)
rma.load("model_ja.json")

# Let's analyze a sample sentence (from http://tatoeba.org/jpn/sentences/show/103809)
# With a disastrous result, since the model is empty!


def tokenizer(text):
    tokens = rma.tokenize(text)
    return tokens
def view_results(tokens):
    for i in range(len(tokens)):
        print(tokens[i][0], tokens[i][1])
text = u"動詞が含まない文節を分析データに入れないという案です。"
tokens = tokenizer(text)
view_results(tokens)