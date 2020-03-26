import numpy as np

# 生成narray数组

# 传入普通数组转化:
list1 = [[1, 2], [2, 3], [4, 1]]
a1 = np.array(list1)
print(type(a1))
print(a1)

# 传入range生成序列
a2 = np.array(range(24))
print(a2)

# np.arange 生成
a3 = np.arange(0, 10, 2)
print(a3)

# 转化成普通数组
print('转化成普通数组')
print(a3.tolist())

'''
# 运行效率对比示例：

a4=[]
for i in range(100000000):
    a4.append(random.random())
t1=time.time()
sum1=sum(a4)
t2=time.time()

a5=np.array(a4)
t3=time.time()
sum2=np.sum(a5)
t4=time.time()
# 0.6655900478363037 0.11892485618591309
print(t2-t1,t4-t3)
'''
