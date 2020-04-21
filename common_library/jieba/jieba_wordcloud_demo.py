import jieba
import pandas as pd
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib.image import imread


# 获取数据
def get_data():
    # pandas读取数据
    df = pd.read_csv("demo/maoyan/asset/comments.csv",
                     names=["id", "nickName", "userLevel", "cityName", "content", "score", "startTime"])
    ser_content = df['content']
    str_content = ','.join(str(val) for val in ser_content)
    return str_content

# 创建停用词list


def get_stopwords_list(filepath):
    stopwords_list = [line.strip() for line in open(
        filepath, 'r', encoding='utf-8').readlines()]
    return stopwords_list


# 对句子进行分词
def seg_sentence(sentence):
    jieba.load_userdict('common_library/jieba/asset/user_dict.txt')
    cut_sentence = jieba.cut(sentence.strip())
    stopwords = get_stopwords_list(
        'common_library/jieba/asset/stopwords.txt')  # 这里加载停用词的路径
    cut_list = []
    for word in cut_sentence:
        if word not in stopwords:
            if word != '\t':
                cut_list.append(word)
    return cut_list


# 对分词进行词频展示
def word_frequency(cut_list, frequency_path):
    frequencies_content = ''
    with open(frequency_path, 'a', encoding='utf-8') as f:
        c = Counter()
        for x in cut_list:
            if len(x) > 1 and x != '\r\n':
                c[x] += 1
        for (k, v) in c.most_common():
            if v > 10:
                frequencies_content = frequencies_content + \
                    '%s %d%s' % (k, v, '\n')
                f.write('%s %d%s' % (k, v, '\n'))
    return frequencies_content


# 根据词频生成词云
def create_word_cloud(frequencies_content):
    # 词云配置
    wc_config = WordCloud(
        font_path='simhei.ttf',
        width=800,
        height=600,
        background_color=None,
    )

    # 生成词云
    word_cloud = wc_config.generate(text=frequencies_content)
    # 保存词云
    word_cloud.to_file("common_library/jieba/asset/cloud2.jpg")
    # 显示词云
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    str_content = get_data()
    cut_list = seg_sentence(str_content)
    frequencies_content = word_frequency(
        cut_list, 'common_library/jieba/asset/count_result.txt')  # 取词频
    create_word_cloud(frequencies_content)
