import time


# class +类名【约定俗成（首字母大写）】(继承的父类)
class Teacher(object):
    # 类属性：直接类里创建的属性，区别于实例属性
    age = 18
    # 私有的类属性：加了__
    __type = '黄种人'

    # 方法：函数在类里面就叫方法
    # 对象方法：有self的为对象方法；
    def show(self):
        print('大家好，我是中国老师')

    # __new__ 创建对象，自动调用的方法
    def __new__(cls, *args, **kwargs):
        print(args,kwargs)
        print('创建完成了新老师')
        return object.__new__(cls)

    # __init__ ：创建完成对象（new）后进行初始化，自动调用的方法
    def __init__(self, name):
        # 实例属性：在__init__方法里定义的属性
        self.name = name
        print('初始化了新的老师:' + name)

    # __str__： 当使用print函数打印对象时候，自动调用的方法
    def __str__(self):
        return "大家好，我是中国老师：%s" % (self.name)

    # __del__： 当对象被销毁（并且引用计数为0），自动调用的方法
    def __del__(self):
        print('销毁： %s' % (self.name))


t1 = Teacher('张三')

print(t1.name)

# 在外部添加属性
t1.sex = '男'
print(t1.sex)

# 调用了：__str__
print(t1)

t2 = t1

print(t2)

# 手动销毁，程序退出也会自动销毁
print('准备销毁t1')
del t1
print('准备销毁t2')
del t2

# 延迟程序自动销毁
time.sleep(3)
print('程序退出了')


