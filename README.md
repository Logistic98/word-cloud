## word-cloud

### 1. 词云简介

词云，又称文字云，是文本数据的视觉表示，由词汇组成类似云的彩色图形，用于展示大量文本数据。 通常用于描述网站上的关键字元数据，或可视化自由格式文本，每个词的重要性以字体大小或颜色显示。在数据可视化方面，词云一直是一种视觉冲击力很强的方式。

### 2. 常见技术方案

对输入的一段文字进行语义分割，得到不同频度的词汇，然后以正比于词频的字体大小无规则的集中显示高频词，简洁直观高效。其中获取词汇我们可以使用 jieba 分词等 NLP 库。渲染部分通常有两种方式，一种是使用 Python 直接渲染成静态图片，另一种是以 RESTful API 的形式返回给前端，使用Echarts进行渲染，这样得到的就是动态词云，鼠标悬浮上去会有特效，会更好看一些。

### 3.  代码讲解及参考

见我的博客：[Python生成静态词云及Echarts动态渲染词云](https://www.eula.club/Python生成静态词云及Echarts动态渲染词云.html)

参考资料：

[1] [Python词云可视化 from CNBLOG](https://www.cnblogs.com/wkfvawl/p/11585986.html)

[2] [词云可视化：四行Python代码轻松上手到精通 from Github](https://github.com/TommyZihao/zihaowordcloud)

[3] [词云可视化：四行Python代码轻松上手到精通 from Bilibili](https://www.bilibili.com/video/av53917673/?p=1)

[4] [你不知道的词云 from python 123](https://python123.io/tutorials/word_cloud)

[5] [纯前端实现词云展示+附微博热搜词云Demo代码 from 稀土掘金](https://juejin.cn/post/7030070889014099999)

[6] [基于 wordcloud2.js 的 Apache ECharts 词云扩展 from Github](https://github.com/ecomfe/echarts-wordcloud)