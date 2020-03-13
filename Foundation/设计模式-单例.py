# 单例：常用的设计模式 - 保证一个类只有一个实例（内存地址同一个）
# 技术上利用一个私有属性(约定俗成__instance)和new即可实现
# 应用场景：发送短信 -- 如果有几十万个用户同时有发送短信的需求，那么该sdk就要重复创建几十万个用于发送短信验证码的对象；网站计数器
# 什么情况下需要单例模式：1.每个实例都会占用资源，而且每个实例初始化都会影响性能；2.当有同步需求的时候，如日志文件的控制，确保只有一个实例。





class Person(object):
    def __init__(self):
        print('初始化Person')


p1 = Person()
p2 = Person()
# 打印内存地址 不同 <__main__.Person object at 0x00000245713AC1C8> <__main__.Person object at 0x00000245713AC288>
print(p1, p2)


class Person2(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        print('初始化Person2')


p3 = Person2()
p4 = Person2()
# 打印内存地址 相同 <__main__.Person2 object at 0x000001E67DA9C888> <__main__.Person2 object at 0x000001E67DA9C888>
print(p3, p4)
