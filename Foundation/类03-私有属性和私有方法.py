# 私有：前端加上__

class Person(object):
    age=18
    def __init__(self):
        self.name='张三'
        self.__sex='男'
    def show(self):
        print('执行show')
    def __show(self):
        print('执行__show')

person=Person()

# 查看所有对象的属性信息
print(person.__dict__)
# 查看类的所有方法和类属性（不包括实例属性）
print(Person.__dict__)
# 私有调用
person._Person__show()
print(person._Person__sex)