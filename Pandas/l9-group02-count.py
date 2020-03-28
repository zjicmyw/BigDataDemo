import pandas as pd
import numpy as np

# 计算分为 聚合和apply
'''聚合函数
mean 计算分组平均值
count 分组中非NA值的数量
sum 非NA值的和
median 非NA值的算术中位数
std 标准差
var 方差
min 非NA值的最小值
max 非NA值的最大值
prod 非NA值的积
first 第一个非NA值
last 最后一个非NA值
mad 平均绝对偏差
mode 模
abs 绝对值
sem 平均值的标准误差
skew 样品偏斜度(三阶矩)
kurt 样品峰度(四阶矩)
quantile 样本分位数(百分位上的值)
cumsum 累积总和
cumprod 累积乘积
cummax 累积最大值
cummin 累积最小值
'''
df1=pd.DataFrame({'Data1':np.random.randint(0,10,5),
                  'Data2':np.random.randint(10,20,5),
                  'key1':list('aabba'),
                  'key2':list('xyyxy')})
'''
   Data1  Data2 key1 key2
0      9     14    a    x
1      2     13    a    y
2      2     13    b    y
3      9     14    b    x
4      2     11    a    y
'''
# 按key1分组，进行聚合计算
# 注意:当分组后进行数值计算时，不是数值类的列会被清除
print(df1.groupby('key1').sum())
'''
      Data1  Data2
key1
a        13     38
b        11     27
'''
# 只算data1
print(df1['Data1'].groupby(df1['key1']).sum())#方法1
print(df1.groupby('key1')['Data1'].sum())#方法2
'''
key1
a    16
b    13
Name: Data1, dtype: int32
'''
# 使用agg()函数 可以同时做多个聚合运算
print(df1.groupby('key1').agg(['sum','mean','std']))
'''
     Data1                     Data2
       sum      mean       std   sum       mean       std
key1
a       16  5.333333  1.527525    40  13.333333  2.886751
b       13  6.500000  3.535534    28  14.000000  4.242641
'''
# 可自定义函数，传入agg方法中 grouped.agg(func)

def peak_range(df):
    return df.max() - df.min()
print(df1.groupby('key1').agg(['mean', ('range', peak_range)])) # 通过元组提 供新的列名

'''
         Data1            Data2
          mean range       mean range
key1
a     2.333333     6  14.333333     5
b     7.000000     4  16.500000     5
'''




# 拓展apply函数
# apply函数是pandas里面所有函数中自由度最高的函数
df1=pd.DataFrame({'sex':list('FFMFMMF'),'smoker':list('YNYYNYY'),'age': [21,30,17,37,40,18,26],'weight':[120,100,132,140,94,89,123]})
'''
  sex smoker  age  weight
0   F      Y   21     120
1   F      N   30     100
2   M      Y   17     132
3   F      Y   37     140
4   M      N   40      94
5   M      Y   18      89
6   F      Y   26     123
'''
def bin_age(age):
    if age >=18:
        return 1
    else:
        return 0
# 抽烟的年龄大于等18的
res1=df1['age'].apply(bin_age)
'''
0    1
1    1
2    0
3    1
4    1
5    1
6    1
Name: age, dtype: int64
'''
df1['age'] = res1 # 将得到的数据赋值
'''
  sex smoker  age  weight
0   F      Y    1     120
1   F      N    1     100
2   M      Y    0     132
3   F      Y    1     140
4   M      N    1      94
5   M      Y    1      89
6   F      Y    1     123
'''
# apply可以传参数
def top(smoker,col,n=2):
    return smoker.sort_values(by=col)[-n:]
print(df1.groupby('smoker').apply(top,col='weight'))# 取出抽烟和不抽烟的体重前二
'''
         sex smoker  age  weight
smoker
N      4   M      N    1      94
       1   F      N    1     100
Y      2   M      Y    0     132
       3   F      Y    1     140
'''