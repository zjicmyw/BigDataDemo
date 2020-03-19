import matplotlib.pyplot as plt
import random
import matplotlib.font_manager as fm

# 折线图/散点图 - 显示温度变化
x = range(2, 26, 2)
y1 = [random.randint(10, 20) for val in x]
y2 = [random.randint(0, 10) for val in x]
y = [random.randint(0, 20) for val in x]
# 设置画布
plt.figure(figsize=(12, 6), dpi=80)
# 设置刻度
x_rulers = ['{}:00'.format(i) for i in x]
plt.xticks(x, x_rulers)
y_rulers = ['{}°C'.format(i) for i in y]
plt.yticks(y, y_rulers)
# 设置标题
# 中文
my_font = fm.FontProperties(fname='C:\Windows\Fonts\msyh.ttc', size=14)
# plt.rcParams['font.sans-serif'] = 'SimHei'
# plt.rcParams['font.size'] = 18
plt.xlabel('时间', color='green', fontproperties=my_font)
plt.ylabel('温度', color='blue', rotation=0, fontproperties=my_font)

plt.title('今日温度一览', fontproperties=my_font)

'''
# 设置折线图样式
plt.plot(x, y1, color='red', alpha=0.3, linestyle='--', linewidth=3, label='max')
plt.plot(x, y2, color='yellow', alpha=0.3, linestyle='-.', linewidth=3, label='最低温')
'''

# 设置散点图样式
plt.scatter(x, y1, color='red', alpha=0.3, linestyle='--', linewidth=3, label='max')
plt.scatter(x, y2, color='yellow', alpha=0.3, linestyle='-.', linewidth=3, label='最低温')

# 设置图例（多条线需要）
# upper  center   lower          |  left right center
plt.legend(loc='upper right', prop=my_font)

plt.savefig('./BigDataDemo/cache/1.png')
# show必须在savefig下
plt.show()
