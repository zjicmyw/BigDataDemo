import numpy as np

''' 
numpy 常见运算
ndarray.min() / np.min(ndarray)
ndarray.max() / np.max(ndarray)
ndarray.mean() / np.mean(ndarray)
ndarray.sum() / np.sum(ndarray)
np.exp()
np.sqrt() 开根号
np.sort() 排序
np.argsort() 排序的索引

'''

# 最大数max最小数min
score = np.array([[82, 72], [77, 42], [99, 100]])
print(score)
print('最大数max最小数min:', np.max(score), np.min(score))
print('轴:', np.max(score, axis=0), np.max(score, axis=1), sep='\n')
# 数据比较(长度相同或者为一个单独数值)
result1 = np.maximum([-1, -5, 2, 7], [3, 4, -3, 2])
result2 = np.minimum([-1, -5, 2, 7], -9)
print(result1)
print(result2)
'''
[[ 82  72]
 [ 77  42]
 [ 99 100]]
最大数max最小数min 100 42
轴 [ 99 100] [ 82  77 100]
[3 4 2 7]
[-9 -9 -9 -9]
'''
result1 = np.mean(score)
result2 = np.mean(score, axis=1)
result3 = score.cumsum(0)
result4 = np.std(score, axis=0)
print('平均值：', result1)
print('行列平均值：', result2)
print('累计和：', result3, sep='\n')
print('标准差：', result4)
'''
[[ 82  72]
 [ 77  42]
 [ 99 100]]
平均值： 78.66666666666667
行列平均值： [77.  59.5 99.5]
累计和： 
[[ 82  72]
 [159 114]
 [258 214]]
 标准差： [ 9.41629793 23.68309289]
'''
