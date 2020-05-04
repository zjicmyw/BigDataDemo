import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker


# pandas读取数据
df = pd.read_csv("demo/maoyan/asset/comments.csv",
                 names=["id", "nickName", "userLevel", "cityName", "content", "score", "startTime"])

attr = ["一星", "二星", "三星", "四星", "五星"]
score = df.groupby("score").size()  # 分组求和

value_list = [
    score.iloc[0] + score.iloc[1] + score.iloc[1],
    score.iloc[3] + score.iloc[4],
    score.iloc[5] + score.iloc[6],
    score.iloc[7] + score.iloc[8],
    score.iloc[9] + score.iloc[10],
]
# #  '《无双》评星比例', title_pos='center', width=900
# pie = Pie()
# # pie.use_theme("dark")
# pie.add("评分", attr, value, center=[60, 50], radius=[25, 75], rosetype='raea', is_legend_show=True, is_label_show=True)
# pie.render('cache/评星.html')

print(value_list)
'''
[37, 6, 123, 686, 2136]
'''
c = (
    Pie()
    .add(
         "",
        [list(z) for z in zip(attr,[37, 6, 123, 686, 2136])],
        center=["20%", "30%"],
        radius=[25, 75],
        rosetype='raea', 
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="《无双》评星比例"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("demo/maoyan/asset/电影无双评星比例.html")
)
