#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import MeCab
#Taggerの引数に-dオプションとmecab-ipadic-neologdの場所を指定する
#　↓場所の確認
# echo `mecab-config --dicdir`"/mecab-ipadic-neologd"
m = MeCab.Tagger("-Ochasen")
text = m.parseToNode("サンプルで使いました！！私には洗浄力が強すぎました。結構顔がツッパリます（＞＿＜）それに値段が・・・もっと安くていいのがあるし。かうことはないでしょう。")
print(text)
