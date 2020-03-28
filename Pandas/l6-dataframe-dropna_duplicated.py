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
df4 = pd.concat([df1, df2], axis=0, ignore_index=True)
'''
     a    b    c    d    e
0  0.0  1.0  NaN  NaN  NaN
1  2.0  3.0  NaN  NaN  NaN
2  4.0  5.0  NaN  NaN  NaN
3  NaN  NaN  0.0  1.0  2.0
4  NaN  NaN  3.0  4.0  5.0
'''

# 过滤dropna
newprint('过滤dropna')
df5 = pd.DataFrame([[1, np.nan], [np.nan, np.nan],
                    [1, 2], [np.nan, 3], [3, 4]])
print(df5)
print(df5.dropna())  # 默认how='any'：只要行内有NaN,就把该行删除
print(df5.dropna(how='all'))  # 一行全部NaN,才删除，
# print(df5.notnull())
# print(df5.isnull())
# 默认axis=0，可设置axis=1,thresh=x，x为如果Nan数量大于等于3就删除该行/列
print(df4.dropna(axis=1, thresh=3))
'''
     0    1
0  1.0  NaN
1  NaN  NaN
2  1.0  2.0
3  NaN  3.0
4  3.0  4.0
     0    1
2  1.0  2.0
4  3.0  4.0
     0    1
0  1.0  NaN
2  1.0  2.0
3  NaN  3.0
4  3.0  4.0
     a    b
0  0.0  1.0
1  2.0  3.0
2  4.0  5.0
3  NaN  NaN
4  NaN  NaN
'''

# 用常数填充NaN df.fillna(num,[inplace=False],[axis=0],[limit=]) 默认生成新的，inplace=True则直接修改df
print(df5.fillna(0))
# 按列填充不同数值
print(df5.fillna({0: 10, 1: 20}))
# 填充指定列
df5.iloc[:, 1].fillna(5, inplace=True)
print(df5)
'''
     0    1
0  1.0  0.0
1  0.0  0.0
2  1.0  2.0
3  0.0  3.0
4  3.0  4.0
      0     1
0   1.0  20.0
1  10.0  20.0
2   1.0   2.0
3  10.0   3.0
4   3.0   4.0
    0    1
0  1.0  5.0
1  NaN  5.0
2  1.0  2.0
3  NaN  3.0
4  3.0  4.0
'''

# 去重
newprint('去重')
df6 = pd.DataFrame({'A': [1, 2, 1, 2, 3, 1], 'B': list('aabcab')})
print(df6)
print(df6.duplicated())  # 判断每一行是否重复
print(df6.drop_duplicates())  # 去掉重复行
print(df6.drop_duplicates(['A']))  # 按列去掉重复行
'''
   A  B
0  1  a
1  2  a
2  1  b
3  2  c
4  3  a
5  1  b
0    False
1    False
2    False
3    False
4    False
5     True
   A  B
0  1  a
1  2  a
2  1  b
3  2  c
4  3  a
dtype: bool
   A  B
0  1  a
1  2  a
4  3  a
'''
