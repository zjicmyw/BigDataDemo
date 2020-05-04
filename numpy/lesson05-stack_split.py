import numpy as np

# 数组的合并、堆叠、水平拼接、竖直拼接
'''
np.append()
np.concatenate()
np.stack()
np.hstack()
np.vstack()
np.dstack()
其中最泛用的是第一个和第二个。第一个可读性好，比较灵活，但是占内存大。第二个则没有内存占用大的问题。
'''
a = np.array([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
])
b = a * 2
# 水平组合
print(np.hstack((a, b)))
print(np.concatenate((a, b), axis=1))
'''
array(［ 0, 1, 2, 0, 2, 4],
       [ 3, 4, 5, 6, 8, 10],
       [ 6, 7, 8, 12, 14, 16］)
'''
# 垂直
print(np.vstack((a, b)))
print(np.concatenate((a, b), axis=0))
'''
array(［ 0, 1, 2],
       [ 3, 4, 5],
       [ 6, 7, 8],
       [ 0, 2, 4],
       [ 6, 8, 10],
       [12, 14, 16］)
'''

# 数组的水平分割、竖直分割
'''
np.hsplit()
np.vsplit()
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
'''
print(np.hsplit(a, 3))
print(np.vsplit(a, 3))
'''
[array([[0],
       [3],
       [6]]), array([[1],
       [4],
       [7]]), array([[2],
       [5],
       [8]])]
[array([[0, 1, 2]]), array([[3, 4, 5]]), array([[6, 7, 8]])]
'''
