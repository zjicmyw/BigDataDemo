import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
 
src_asset='demo/maoyan/asset/'

df = pd.read_csv(src_asset+"comments.csv",
                 names=["id", "nickName", "userLevel", "cityName", "content", "score", "startTime"])

ser_city = df['cityName']
str_city=','.join(ser_city.astype(str).tolist())
# 词云配置
wc_config = WordCloud(
        font_path='simhei.ttf', 
        width=800, 
        height=600, 
        background_color=None
        )

# 生成词云
word_cloud=wc_config.generate(text=str_city)
# 保存词云
word_cloud.to_file(src_asset+"cloud1.jpg")  # 保存图片
# 显示词云
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis('off')
plt.show()


