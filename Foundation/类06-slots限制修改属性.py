class Teacher(object):
    # 类属性：直接类里创建的属性，区别于实例属性
    age = 18
    # 私有的类属性：加了__
    __type = '黄种人'

    # slots限制了只能修改name
    __slots__ = ('name')

    # __init__ ：创建完成对象（new）后进行初始化，自动调用的方法
    def __init__(self, name):
        # 实例属性：在__init__方法里定义的属性
        self.name = name
        print('初始化了新的老师:' + name)


t1 = Teacher('张三')

# 报错，slots限制了只能修改name
# t1.sex='男'
# t1.age=28
t1.name = '李四'
