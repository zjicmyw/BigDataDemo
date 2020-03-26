import matplotlib.pyplot as plt
import random
import matplotlib.font_manager as fm

# 柱状图显示多日平均气温
x = ['1日', '2日', '3日', '4日', '5日']
y = [random.randint(0, 30) for val in x]
# 设置画布
plt.figure(figsize=(12, 6), dpi=80)
# 中文
my_font = fm.FontProperties(fname='C:\Windows\Fonts\msyh.ttc', size=14)

# 设置刻度 x轴的刻标以及对应的标签
plt.xticks(range(len(x)), x, fontproperties=my_font)
y_rulers = ['{}°C'.format(i) for i in y]
plt.yticks(y, y_rulers)
# 设置标题
plt.xlabel('日期', color='green', fontproperties=my_font)
plt.ylabel('温度', color='blue', rotation=0, fontproperties=my_font)

plt.title('多日平均气温', fontproperties=my_font)

# 设置柱状图样式
rects = plt.bar(x, y, width=0.3)
for rect in rects:
    height = rect.get_height()
    # x轴位置，y轴高度+0.3，显示的数值
    plt.text(rect.get_x() + rect.get_width() / 2, height + 0.2, str(height), ha='center')
    print(rect.get_x() + rect.get_width() / 2, height + 0.3, str(height))

plt.savefig('./BigDataDemo/cache/2.png')
# show必须在savefig下
plt.show()
