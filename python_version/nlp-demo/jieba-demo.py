# -*- coding: utf-8 -*-

import jieba

text = '动力学和电磁学'

print('{:-^50}'.format('精确模式：每个字只用一遍，不存在冗余词汇'))
textlist = jieba.lcut(text)
print('分词之后生成的列表为', textlist)

print('{:-^50}'.format('全模式：把每个字可能形成的词汇都提取出来，存在冗余'))
textlist = jieba.lcut(text, cut_all=True)
print('分词之后生成的列表为', textlist)

print('{:-^50}'.format('搜索引擎模式：将全模式分词的结果从短到长排列好'))
textlist = jieba.lcut_for_search(text)
print('分词之后生成的列表为', textlist)

