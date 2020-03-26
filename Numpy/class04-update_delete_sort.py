import numpy as np

# 数组的添加、删除、去重
print('添加')
score = np.array([[82, 72], [77, 42], [99, 100]])
a1 = np.append(score, [[66, 55], [99, 77]])
print(a1)
a2 = np.append(score, [[66, 55]], axis=0)
print(a2)
print('删除每一行的第二列')
a3 = np.delete(score, 1, axis=1)
print(a3)
print('去重并且排序')
print(a1)
print(np.unique(a1))
u, u2 = np.unique(a1, return_inverse=True)
print(u)
'''
return_index=True, 新列表元素在旧列表下标
return_inverse=True, 旧列表元素在新列表下标
return_counts=True，旧列表出现次数
'''
print(u2)
