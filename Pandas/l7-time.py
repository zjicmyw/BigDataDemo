import pandas as pd
import numpy as np

# 1.生成一段时间范围
'''
date_range函数主要用于生成一个固定频率的时间索引，在调用构造方法时，必须指定start，end，periods中的两个参数值，否则报错
frep：日期偏移量，取值为string,默认为“D”
periods:生成时间数量，取值为整数或者None
closed：选择是否包含开始和结束时间closed = None，left包含开始时间，不包含结束时间，right与之相反
'''

# 时间序列频率：
'''D：日历中的每天 
B：工作日的每天
H:每小时 
T或min:每分钟 
S ：每秒 
L或ms：每毫秒 
U: 每微妙
M: 日历中的月底日期
BM ： 工作日的月底日期
MS： 日历中的月初日期 
BMS： 工作日的月初日期
'''

date = pd.date_range(start='20200301', end='20200302',
                     freq='2H30T', closed='right')
date1 = pd.date_range(start='20200301', periods=3, freq='3B')
'''
DatetimeIndex(['2020-03-01 02:30:00', '2020-03-01 05:00:00',
               '2020-03-01 07:30:00', '2020-03-01 10:00:00',
               '2020-03-01 12:30:00', '2020-03-01 15:00:00',
               '2020-03-01 17:30:00', '2020-03-01 20:00:00',
               '2020-03-01 22:30:00'],
              dtype='datetime64[ns]', freq='150T')
DatetimeIndex(['2020-03-02', '2020-03-05', '2020-03-10'], dtype='datetime64[ns]', freq='3B')
'''

# 2时间序列在dataframe中的作用

# 可将时间序列作为索引
index1 = pd.date_range(start='20200301', periods=7)
df = pd.Series(np.random.randint(0, 7, size=7), index=index1)
'''
2020-03-01    4
2020-03-02    0
2020-03-03    3
2020-03-04    5
2020-03-05    2
2020-03-06    2
2020-03-07    2
Freq: D, dtype: int32
'''
# truncate时间过滤
before = df.truncate(before='2020-03-04')
after = df.truncate(after='2020-03-04')
'''
2020-03-04    5
2020-03-05    2
2020-03-06    2
2020-03-07    2
Freq: D, dtype: int32
2020-03-01    4
2020-03-02    0
2020-03-03    3
2020-03-04    5
Freq: D, dtype: int32
'''
long_ts = pd.Series(np.random.randn(
    1000), index=pd.date_range('1/1/2019', periods=1000))

# 获取数据：
# 根据年份获取
result = long_ts['2020']
# 年份和日期获取
result1 = long_ts['2020-05']
# 使用切片
result2 = long_ts['2020-05-01':'2020-05-07']
# 通过between_time()返回位于指定时间段的数据集
index = pd.date_range('2020-03-17', '2020-03-18', freq='2H')
ts = pd.Series(np.random.randn(len(index)), index=index)
'''
2020-03-17 08:00:00   -0.105823
2020-03-17 10:00:00   -0.239439
2020-03-17 12:00:00    0.423299
2020-03-17 14:00:00    1.467829
'''
