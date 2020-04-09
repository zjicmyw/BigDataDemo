import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

pie1 = (
    Pie()
    .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("cache/pie_base.html")
)
