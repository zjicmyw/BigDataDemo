def newprint(content):
    print('-' * 30)
    print(content, ':')


# 装饰器：语法糖
newprint('装饰器：语法糖')


def alert(new_func):
    def func_inner():
        print('这是内部函数')
        new_func()

    return func_inner


@alert  # 语法糖
def show():
    print('传入函数')


show()
show()

# 装饰器修饰，带有参数的函数

newprint('装饰器修饰，带有参数的函数')


def alert(new_func):
    def func_inner(title, content):
        print('弹出框：')
        new_func(title, content)

    return func_inner


@alert  # 语法糖
def show(title, content):
    print('提醒：', title, '----', '详情：', content)


show('警告3', '数据库连不上')

# 装饰器修饰不定长参数的函数
newprint('装饰器修饰不定长参数的函数')


def func_cluc(new_func):
    def inner(*args, **kwargs):
        print('计算结果如下:', end='')  # end为空，消除了自动换行，让结果在同一行
        return new_func(*args, **kwargs)

    return inner


@func_cluc
def sum2(n1, n2):
    return n1 + n2


@func_cluc
def sum3(n1, n2, n3):
    return n1 + n2 + n3


print(sum2(2, 3))
print(sum3(2, 3, 4))

# 定义一个带有参数的的装饰器函数
newprint('装饰器修饰不定长参数的函数')


def func_outer(char):
    def func_middle(new_func):
        def func_inner():
            print(char)
            new_func()

        return func_inner

    return func_middle


@func_outer('hello ')
def show():
    print('world')


show()
