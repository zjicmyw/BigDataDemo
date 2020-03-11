# 高阶函数：一个函数的参数，可以接收另一个函数 or 返回一个函数（返回函数）

def func_sum(n1, n2):
    return n1 + n2


def calc_num(new_func):
    return print(new_func(2, 1))


calc_num(func_sum)


# 超级高阶 把or变成& 同时满足or两边的也是高阶函数

def func_outer(new_func):
    new_func()

    def func_inner():
        print('执行内部函数')

    return func_inner


def func_new():
    print('执行外部传入函数')


func_final = func_outer(func_new)

func_final()
func_final()
