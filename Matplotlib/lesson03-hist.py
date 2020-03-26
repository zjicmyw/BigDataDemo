import matplotlib.pyplot as plt
import random
import matplotlib.font_manager as fm
import numpy as np

# 直方图 显示数据分布 统计

#生成【0-100】之间的100个数据,即 数据集
x=np.random.randint(0,100,100)
#设置连续的边界值，即直方图的分布区间[0,10],[10,20]...
bins=np.arange(0,101,10)

# 设置画布
plt.figure(figsize=(12, 6), dpi=80)
# 中文
my_font = fm.FontProperties(fname='C:\Windows\Fonts\msyh.ttc', size=14)


# 设置标题
plt.xlabel('区间', color='green', fontproperties=my_font)
plt.ylabel('数量', color='blue', rotation=0, fontproperties=my_font)

plt.title('统计', fontproperties=my_font)

# 设置直方图样式
plt.hist(x,bins,color='fuchsia',alpha=0.5)

plt.savefig('./BigDataDemo/cache/3.png')
# show必须在savefig下
plt.show()
