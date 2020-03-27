import pandas as pd
from pandas import Series, DataFrame
import numpy as np


def newprint(content):
    print('-' * 30)
    print(content, ':')


# 合并concat
newprint('合并concat')
df1 = pd.DataFrame(np.arange(6).reshape(3, 2), columns=['a', 'b'])
df2 = pd.DataFrame(np.arange(6).reshape(2, 3), columns=['c', 'd', 'e'])
print(df1, df2, sep='\n')
df3 = pd.concat([df1, df2], axis=1)
print(df3)
df4 = pd.concat([df1, df2], axis=0, ignore_index=True)
print(df4)  # 垂直
'''
   a  b
0  0  1
1  2  3
2  4  5
   c  d  e
0  0  1  2
1  3  4  5
   a  b    c    d    e
0  0  1  0.0  1.0  2.0
1  2  3  3.0  4.0  5.0
2  4  5  NaN  NaN  NaN
     a    b    c    d    e
0  0.0  1.0  NaN  NaN  NaN
1  2.0  3.0  NaN  NaN  NaN
2  4.0  5.0  NaN  NaN  NaN
3  NaN  NaN  0.0  1.0  2.0
4  NaN  NaN  3.0  4.0  5.0
'''
print('join:')
df1 = pd.DataFrame(np.arange(6).reshape(3, 2), columns=[
                   'a', 'b'], index=['A', 'B', 'C'])
df2 = pd.DataFrame(np.arange(6).reshape(2, 3), columns=[
                   'c', 'd', 'e'], index=['A', 'D'])
print(df1, df2, sep='\n')
print(df1.join(df2))
print(df1.join(df2, how='right'))
print(df1.join(df2, how='outer'))  # pd.concat([df1, df2], axis=1)
'''
   a  b
A  0  1
B  2  3
C  4  5
   c  d  e
A  0  1  2
D  3  4  5
   a  b    c    d    e
A  0  1  0.0  1.0  2.0
B  2  3  NaN  NaN  NaN
C  4  5  NaN  NaN  NaN
     a    b  c  d  e
A  0.0  1.0  0  1  2
D  NaN  NaN  3  4  5
     a    b    c    d    e
A  0.0  1.0  0.0  1.0  2.0
B  2.0  3.0  NaN  NaN  NaN
C  4.0  5.0  NaN  NaN  NaN
D  NaN  NaN  3.0  4.0  5.0
'''
dict1 = {
    '名称': ['AA', 'BB', 'CC', 'DD', 'EE'],
    '性别': ['男', '男', '女', '女', '男'],
    '职称': ['教授', '副教授', '教师', '教师', '教师']
}
df1 = pd.DataFrame(data=dict1, index=range(101, 106))
df1.columns.name = '老师'
df1.index.name = 'id'
dict2 = {
    '名称': ['BB', 'AA', 'DD', 'CC', 'FF'],
    '课名': ['数学', '语文', '英语', '历史', '体育'],
}
df2 = pd.DataFrame(data=dict2, index=range(201, 206))
df2.columns.name = '课程'
df2.index.name = 'id'

print('merge:')
print(df1, df2, sep='\n')
'''
   名称 性别   职称  课名
0  AA  男   教授  语文
1  BB  男  副教授  数学
2  CC  女   教师  历史
3  DD  女   教师  英语
4  EE  男   教师  体育
   名称 性别   职称  课名
0  AA  男   教授  语文
1  BB  男  副教授  数学
2  CC  女   教师  历史
3  DD  女   教师  英语
4  EE  男   教师  体育
'''
print(pd.merge(df1, df2, how='left'))
print(pd.merge(df1, df2, how='right'))

'''
   名称 性别   职称   课名
0  AA  男   教授   语文
1  BB  男  副教授   数学
2  CC  女   教师   历史
3  DD  女   教师   英语
4  EE  男   教师  NaN
   名称   性别   职称  课名
0  AA    男   教授  语文
1  BB    男  副教授  数学
2  CC    女   教师  历史
3  DD    女   教师  英语
4  FF  NaN  NaN  体育
'''

dict3 = {
    '名称': ['BB', 'AA', 'DD', 'CC', 'FF'],
    '课名': ['数学', '语文', '英语', '历史', '体育'],
    '职称': ['教授', '副教授', '教师', '教师', '教师']
}
df3 = pd.DataFrame(data=dict3, index=range(201, 206))


print(pd.merge(df1, df3, on='名称', suffixes=['_1', '_2']))  # 默认how='innner'
print(pd.merge(df1, df3, on=['名称', '职称']))
'''
   名称 性别 职称_1  课名 职称_2
0  AA  男   教授  语文  副教授
1  BB  男  副教授  数学   教授
2  CC  女   教师  历史   教师
3  DD  女   教师  英语   教师
   名称 性别  职称  课名
0  CC  女  教师  历史
1  DD  女  教师  英语
'''
