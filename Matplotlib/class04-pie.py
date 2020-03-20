import matplotlib.pyplot as plt
import random
import matplotlib.font_manager as fm


# 中文
plt.rcParams['font.sans-serif']=['SimHei']

# 饼状图

labels = ['娱乐','育儿','饮食','房贷','交通','其它']
sizes = [2,5,12,70,2,9]
explode = (0,0,0,0.1,0,0)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=150)
plt.title("饼图示例-8月份家庭支出")
plt.axis('equal')   #该行代码使饼图长宽相等
plt.savefig('./BigDataDemo/cache/4.png')
# show必须在savefig下
plt.show()

'''
pie 函数格式：
def pie(x, explode=None, labels=None, colors=None, autopct=None,
        pctdistance=0.6, shadow=False, labeldistance=1.1, startangle=None,
        radius=None, counterclock=True, wedgeprops=None, textprops=None,
        center=(0, 0), frame=False, rotatelabels=False, hold=None, data=None)


    x: (每一块)
    的比例，如果sum(x) > 1
    会使用sum(x)
    归一化；
    labels: (每一块)
    饼图外侧显示的说明文字；
    explode: (每一块)
    离开中心距离；
    startangle: 起始绘制角度, 默认图是从x轴正方向逆时针画起, 如设定 = 90
    则从y轴正方向画起；
    shadow: 在饼图下面画一个阴影。默认值：False，即不画阴影；
    labeldistance: label标记的绘制位置, 相对于半径的比例，默认值为1
    .1, 如 < 1
    则绘制在饼图内侧；
    autopct: 控制饼图内百分比设置, 可以使用format字符串或者format
    function
    '%1.1f'
    指小数点前后位数(没有用空格补齐)；
    pctdistance: 类似于labeldistance, 指定autopct的位置刻度, 默认值为0
    .6；
    radius: 控制饼图半径，默认值为1；
    counterclock ：指定指针方向；布尔值，可选参数，默认为：True，即逆时针。将值改为False即可改为顺时针。
    wedgeprops ：字典类型，可选参数，默认值：None。参数字典传递给wedge对象用来画一个饼图。例如：wedgeprops = {'linewidth': 3}
    设置wedge线宽为3。
    textprops ：设置标签（labels）和比例文字的格式；字典类型，可选参数，默认值为：None。传递给text对象的字典参数。
    center ：浮点类型的列表，可选参数，默认值：(0, 0)。图标中心位置。
    frame ：布尔类型，可选参数，默认值：False。如果是true，绘制带有表的轴框架。
    rotatelabels ：布尔类型，可选参数，默认为：False。如果为True，旋转每个label到指定的角度。
'''