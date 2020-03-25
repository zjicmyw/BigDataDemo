import numpy as np

# 数组的计算
# 普通加减乘除，广播到所有元素
a1 = np.array(range(24)).reshape(6, 4)
print(a1 + 5)

# 数组间的计算
print('数组间的计算')
a2 = np.arange(24).reshape(6, 4)
print(a2)
a3 = np.arange(100, 124).reshape(6, 4)
print(a3)
# 相同纬度
print('相同纬度')
print(a2 + a3)
# 不同纬度间：必须要一维(行数或者列数需要相同)
print('不同纬度间：必须要一维')
a4 = np.arange(4)
print(a2, a4, a2 * a4, sep='\n')

print('0轴求和')
a5 = np.arange(6).reshape(2, 3)
print(a5, np.sum(a5, axis=0), sep='\n')

print('索引-切片')
a6 = np.array(range(24))
print(a6[1:5:1])
print(a6[3])
print(a6[10:])

a7 = a6.reshape(4, 6)
print(a7)
print(a7[[1, 1, 3], [2, 3, 4]])

print('修改')
a6[10:] = 99
print(a6)
'''
and &
or |
not -
三目运算：
'''
a6[(a6 < 5) | (a6 > 10)] = 0
print(a6)

score = np.array([[82, 72], [77, 42], [99, 100]])
result = np.where(score > 75, 'pass', 'not pass')
print(result)
