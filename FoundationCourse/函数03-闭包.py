# 闭包：闭包本质上也是高阶函数
# 在函数嵌套的前提下，内部函数是使用了外部函数的参数or       变量，并且把内部函数返回。

def newprint(content):
    print('-' * 30)
    print(content, ':')


# 简单的闭包
newprint('简单的闭包')


def func_outer(n1):
    n2 = 2

    def func_inner():
        # 使用了外部函数的参数 and 变量
        print(n1 + n2)

    return func_inner


func_final = func_outer(1)

func_final()

# 闭包的应用场景
newprint('闭包的应用场景')


def alert(title, content):
    def func_inner():
        return print('提醒：', title, '----', '详情：', content)

    return func_inner


new_func1 = alert('警告1', '网络不好')
new_func2 = alert('警告2', '没有数据')

new_func1()
new_func2()

# 装饰器：本质就是闭包：改变了原来函数的功能
newprint('装饰器：本质就是闭包：改变了原来函数的功能')


def show():
    print('执行show函数')


def alert(title, content):
    def func_inner():
        return print('提醒：', title, '----', '详情：', content)

    return func_inner


# 覆盖掉原来的show
show = alert('警告3', '数据库连不上')
show()
