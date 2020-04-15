import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib.image import imread

# pandas读取数据
df = pd.read_csv("demo/maoyan/asset/comments.csv",
                 names=["id", "nickName", "userLevel", "cityName", "content", "score", "startTime"])

ser_city = df['cityName']
str_city=','.join(str(val) for val in ser_city)

mask_img=imread('common_library/wordcloud/asset/background.jfif')#需要白底图

# 词云配置
wc_config = WordCloud(
        font_path='simhei.ttf', 
        width=800, 
        height=600, 
        background_color=None,
        mask=mask_img,# 词云形状
        )

# 生成词云
word_cloud=wc_config.generate(text=str_city)
# 保存词云
word_cloud.to_file("common_library/wordcloud/asset/cloud1.jpg")  # 保存图片
# 显示词云
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis('off')
plt.show()
 
# 保存文件

