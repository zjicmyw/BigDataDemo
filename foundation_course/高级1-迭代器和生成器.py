# 可迭代对象：可用for循环遍历取值的对象：列表[]、元组()、字典{}、字符串、集合、range

# 判断对象是否是可迭代对象
from collections.abc import Iterable

# isinstanche可以判断是否是指定类型
print(isinstance(1, int))
print(isinstance('1', int))
print(isinstance([1, 2], Iterable))

# 可迭代对象都有__iter__方法,查看方法：
print(dir([1, 2]))


# 迭代器：类里有一个__iter__方法和__next__方法,这个类创建的对象就是迭代器
# 优点:节省内存 优点:节省内存 优点:节省内存  重要的事情说三遍
# 应用场景：假设列表有一万数据，for循环遍历取值用迭代器比列表 就省内存多了
class TestIterable(object):
    def __init__(self):
        self.list = [1, 2, 4]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.list):
            result = self.list[self.index]
            self.index += 1
            return result
        else:
            print('抛出异常')
            raise StopIteration


ti1 = TestIterable()
print(isinstance(ti1, Iterable))
print(next(ti1))
print('for循环')
for value in ti1:
    print(value)

# 生成器：特殊的迭代器
print(' 生成器：特殊的迭代器，加入类似列表生成式的概念')
# 先看普通对得列表生成式
result = [value for value in range(3)]
# 类似列表生成式的  生成器创建
result = (value for value in range(3))

print(next(result))
for value in result:
    print(value)


# 使用yield创建生成器,yield可以同时返回多次循环的值,return只能一次
def create():
    for value in range(3):
        yield value


c1 = create()
for value in c1:
    print(value)
