import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib.image import imread

with open("cache/befull523.txt", 'r', encoding='utf-8') as f:
    data = f.read()
    # print(data)


mask_img = imread('common_library/wordcloud/asset/tree.jpg')  # 需要白底图

# 词云配置
wc_config = WordCloud(
    font_path='simhei.ttf',
    width=800,
    height=600,
    background_color=None,
    mask=mask_img,  # 词云形状
)

# 生成词云
word_cloud = wc_config.generate(text=data)
# 保存词云
word_cloud.to_file("cache/befull523.jpg")
# 显示词云
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis('off')
plt.show()
