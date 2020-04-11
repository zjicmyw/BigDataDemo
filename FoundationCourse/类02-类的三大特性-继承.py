# 类的三大特性：封装、继承、多态

def newprint(content):
    print('-' * 30)
    print(content, ':')


# 单继承：一个父类
newprint('单继承')


# 子类复用父类的属性和方法
class Person(object):
    def __init__(self):
        self.age = 18

    def show(self):
        print('Person的年龄', self.age)

    def show11(self):
        print('执行Personshow11', self.age)


class Student(Person):
    pass


stu1 = Student()
stu1.show()
print(stu1.age)


class ScienceStudent(Person):
    # 子类重写了__init__时，就不会调用父类已经定义的__init__
    def __init__(self):
        self.subject = 'Science'


stu2 = ScienceStudent()
# 报错
# print(stu2.age, stu2.subject)


# 多继承：多个父类
newprint('多继承')


class Man(object):
    def __init__(self):
        self.sex = '男'

    def show(self):
        print('Man', self.sex)

    def show2(self):
        print('执行show2')


class ManPerson(Person, Man):
    pass


# stu3，只继承了Person的实例属性，和person、man的方法，但父类方法重名，取第一个
stu3 = ManPerson()
# 报错 'ManPerson' object has no attribute 'sex'
# print(stu3.age,stu3.sex)
stu3.show()
stu3.show2()

# 重写：父类的方法满足不了子类：寻找顺序-从下到上
newprint('重写')


class NewPerson(Person):
    def show(self):
        print('NewPerson的年龄', self.age)


stu4 = NewPerson()
stu4.show()
stu4.show11()

# 查看继承关系  【类名】.mro()
print(NewPerson.mro())

# 在子类中调用父类方法的三种方式
newprint('在子类中调用父类方法')


class NewPerson2(Person):
    def show2(self):
        self.show()

    def show3(self):
        Person.show(self)

    def show4(self):
        # super([指定类的在继承链上下一个类],[继承链])如果是单继承，可以简写super().show()
        super(NewPerson2, self).show()
        # 继承链
        print(self.__class__.mro())


stu5 = NewPerson2()
stu5.show2()
stu5.show3()
stu5.show4()

# 子类重写__init__后，继续使用super调用父类__init__
newprint('子类重写__init__后，继续使用super调用父类__init__')


class Person2(object):
    def __init__(self, name):
        self.name = name
        print(self.name)


class New1Person2(Person2):
    def __init__(self):
        super().__init__('李四')


stu6 = New1Person2()
