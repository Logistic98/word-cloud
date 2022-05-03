# -*- coding: utf-8 -*-

import snownlp

text1 = '中华民族伟大复兴'
print('{:-^50}'.format('测试文本：'+text1))
s = snownlp.SnowNLP(text1)
print('情感分析', s.sentiments)
print('中文分词', s.words)
print('转成拼音', s.pinyin)
print('词频', s.tf)
print('提取三个关键词', s.keywords(3))

text2 = '快递慢到死，客服态度不好，退款！'
print('{:-^50}'.format('测试文本：'+text2))
s = snownlp.SnowNLP(text2)
print('情感分析', s.sentiments)
print('中文分词', s.words)
print('转成拼音', s.pinyin)
print('词频', s.tf)
print('提取三个关键词', s.keywords(3))

