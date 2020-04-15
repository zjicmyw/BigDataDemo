import jieba
import pandas as pd
from collections import Counter


# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


# 对句子进行分词
def seg_sentence(sentence):
    jieba.load_userdict('common_library/jieba/asset/user_dict.txt')
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist('common_library/jieba/asset/stopwords.txt')  # 这里加载停用词的路径
    outstr = []
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr.append(word)
    return outstr


# 对分词进行词频展示
def word_frequency(line_seg):
    c = Counter()
    for x in line_seg:
        if len(x) > 1 and x != '\r\n':
            c[x] += 1
    for (k, v) in c.most_common():
        print('%s%s  %d' % (' ' * (5 - len(k)), k, v))


# pandas读取数据
df = pd.read_csv("demo/maoyan/asset/comments.csv",
                 names=["id", "nickName", "userLevel", "cityName", "content", "score", "startTime"])

ser_city = df['content']
str_city=','.join(str(val) for val in ser_city)

# inputs = open('C:\\Users\EDZ\Desktop\福莱数据第一期\data\迪丽热巴.txt', 'r', encoding='utf-8')
# lines = ""
# for line in inputs:
#     lines += line.replace("\n", "")
# inputs.close()
line_seg = seg_sentence(str_city)  # 这里的返回值是列表
word_frequency(line_seg)  # 取词频