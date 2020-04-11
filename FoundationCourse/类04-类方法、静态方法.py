import time


# class +类名【约定俗成（首字母大写）】(继承的父类)
class Teacher(object):
    # 类属性：直接类里创建的属性，区别于实例属性
    age = 18
    # 私有的类属性：加了__
    __type = '黄种人'

    # 方法：函数在类里面就叫方法
    # 对象方法：有self的为对象方法；
    def object_show(self):
        print('大家好，我是中国老师')

    # 类方法：用关键字@classmethod修饰的方法
    # 场景1：修改类属性
    @classmethod
    def set_age(cls, age):
        cls.age = age
        print('修改年龄为',cls.age)

    @classmethod
    def set_type(cls, type):
        cls.__type = type
        print('修改类型为', cls.__type)

    # 场景2：获得私有的类属性
    @classmethod
    def get_p_type(cls):
        return cls.__type

    # 静态方法：用关键字@staticmethod修饰的方法，和当前对象、类没有关系
    @staticmethod
    def static_show():
        print('我是静态方法')


t1 = Teacher()
t1.set_age(11)
print(t1.get_p_type())

# 私有类方法无法直接用对象或者类获取，会报错
# print(t1.__type)
# print(Teacher.__type)
print(Teacher.age)
print(t1.age)

Teacher.set_age(13)
Teacher.set_type('白种人')
print(t1.get_p_type())
print(Teacher.get_p_type())

