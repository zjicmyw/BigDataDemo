import pandas as pd
from pandas import Series, DataFrame
import numpy as np

'''
算数运算,+-*/
根据index进行计算，没有相同index的返回NaN
'''
print('Series之间的计算')
sel1 = pd.Series([1, 2, 3, 4], ['a', 'b', 'c', 'd'], )
sel2 = pd.Series([1, 2, 3, 4], ['e', 'f', 'a', 'c'])
print(sel1 - sel2)
'''
a   -2.0
b    NaN
c   -1.0
d    NaN
e    NaN
f    NaN
'''

print(sel1 > 2)
print(sel1 * 2)
'''
dtype: float64
a    False
b    False
c     True
d     True
dtype: bool
a    2
b    4
c    6
d    8
dtype: int64
'''

# 和numpy一起使用
print(np.square(sel1))
'''
a     1
b     4
c     9
d    16
dtype: int64
'''
