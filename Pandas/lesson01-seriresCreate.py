import pandas as pd
from pandas import Series, DataFrame
import numpy as pn

'''
Pandas 基于 Series(一维),DataFrame（二维）
'''
# 创建方法1： index有默认数值01234...
print('创建方法1:')
sel = Series(data=[[1, 2], [3, 4], [5, 6]], index=['hah', 'b', 'cc'])
print(sel)
print(type(sel))
print(sel.values)
print(sel.index)
'''
hah    [1, 2]
b      [3, 4]
cc     [5, 6]
dtype: object
<class 'pandas.core.series.Series'>
[list([1, 2]) list([3, 4]) list([5, 6])]
Index(['hah', 'b', 'cc'], dtype='object')
'''
print(list(sel.iteritems()))
'''
[('hah', [1, 2]), ('b', [3, 4]), ('cc', [5, 6])]
'''
# 创建方法2： 传入字典
print('创建方法2： 传入字典')
dict = {'a': 1, 'b': 22, 'c': 333, 'd': 4444}
sel = Series(dict)
print(sel)
'''
a      1
b     22
c    333
d   4444
dtype: int64
'''

# 获取数据
print('获取方法1： 索引下标:', sel[['a', 'c']], sep='n')
print('获取方法2： 位置下标:', sel[1], sep='n')
print('切片:', sel[1:4], sep='n')
print('切片:', sel['b':'d'], sep='n')

# 修改索引
sel.index = ['hah', 'b', 'cc', 'ddd']
print(sel)

# 删除
sel2 = sel.drop(['cc'])
print(sel2)
