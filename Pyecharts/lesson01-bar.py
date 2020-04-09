from pyecharts.charts import Bar

# -------------------------------------
# 官方文档
# https://pyecharts.org/#/zh-cn
# pyecharts是一款将python与echarts结合的强大的数据可视化工具，由于v0.5.x 和 V1 间不兼容，网上大多文章为v0.5.x
# 
# 图标示例
# https://github.com/pyecharts/pyecharts-gallery
# -------------------------------------

bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
bar.render('../cache/bar1.html')