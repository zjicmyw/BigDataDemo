import pandas as pd
from pandas import Series, DataFrame
import numpy as np

# 创建方法1
df1 = pd.DataFrame(data=[[2, 3, 4], [6, 7, 8], [9, 0, 1]], index=[
                   'a', 'b', 'c'], columns=['A', 'B', 'C'])
print(df1)
'''
   A  B  C
a  2  3  4
b  6  7  8
c  9  0  1
'''
# 创建方法2：传入字典
dict = {
    'province': ['GD', 'ZJ', 'SH'],
    'code': ['0571', '1128', '0283'],
    'id': [11, 12, 13]
}
df2 = pd.DataFrame(data=dict, index=[1, 2, 3])
# from_dict 不能写index，默认
df3 = pd.DataFrame.from_dict(dict)
print(df2)
print(df3)
'''
  province  code  id
1       GD  0571  11
2       ZJ  1128  12
3       SH  0283  13
  province  code  id
0       GD  0571  11
1       ZJ  1128  12
2       SH  0283  13

'''

# 获取行列数
print(df2.shape)
# 获取行列索引
print(list(df2.index))
print(list(df2.columns))
# 获取每一列数据类型
print(df2.dtypes)
# 获取纬度
print(df2.ndim)
'''
(3, 3)
[1, 2, 3]
['province', 'code', 'id']
province    object
code        object
id           int64
dtype: object
2
'''
print(df2.values)
'''
[['GD' '0571' 11]
 ['ZJ' '1128' 12]
 ['SH' '0283' 13]]
'''
# 获取所有信息
print(df2.info())
# 获取限定行数据 head tail
print(df2.head(2))
print(df2[0:2])
'''
  province  code  id
1       GD  0571  11
2       ZJ  1128  12
'''
# 获取指定列
print(df2['province'])

# 获取指定多行多列
print(df2[0:2][['province', 'code']])
'''
1    GD
2    ZJ
3    SH
Name: province, dtype: object
 province  code
1       GD  0571
2       ZJ  1128
'''

# 通过索引获取
print('通过索引获取')
print(df2.loc[[1, 2], ['province', 'id']])
print(df2.loc[1, :])
'''
  province  id
1       GD  11
2       ZJ  12

province      GD
code        0571
id            11
'''
# 通过位置获取
print('通过位置获取')
print(df2.iloc[0:2])
