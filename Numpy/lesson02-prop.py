import numpy as np
import random
import time

# 传入普通数组转化:
list1 = [[1, 2], [2, 3], [4, 1]]
a1 = np.array(list1)
print(type(a1))
print(a1)

# 传入range生成序列
a2 = np.array(range(24))
print(a2)

# 常用属性
# 获取数组纬度
print(a1.ndim)
# 获取 行和列
print(a1.shape)
# 获取大小=行*列
print(a1.size)
# 属性可以修改
a1.shape = (2, 3)
print(a1)
# 属性新生成
print('属性新生成')
print(a1.reshape(1, 6))
print(a1.reshape(6, 1))
print(a1.reshape(6, ))
# order='F'以列展开，默认'C'行
print(a1.reshape((6,), order='F'))
# 语法糖：多纬数组转一维
print(a1.flatten(order='F'))
# 三维数组：块、行、列
print(a2.reshape(2, 3, 4))

# 数组的计算
# 普通加减乘除，广播到所有元素
