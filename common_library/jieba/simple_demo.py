import jieba
from collections import Counter

s = '我想和女朋友一起去北京故宫博物院参观和闲逛。'

# 精确模式
cut1 = ','.join(jieba.cut(s))
print(cut1)

# 全模式
cut2=','.join(jieba.cut(s,cut_all = True))
print(cut2)

# 搜索引擎模式
cut3=','.join(jieba.cut_for_search(s))
print(cut3)

'''
我,想,和,女朋友,一起,去,北京故宫博物院,参观,和,闲逛,。
我,想,和,女朋友,朋友,一起,去,北京,北京故宫,北京故宫博物院,故宫,故宫博物院,博物,博物院,参观,和,闲逛,。
我,想,和,朋友,女朋友,一起,去,北京,故宫,博物,博物院,北京故宫博物院,参观,和,闲逛,。
'''

c = Counter(santi_words).most_common(20)
print(c)
