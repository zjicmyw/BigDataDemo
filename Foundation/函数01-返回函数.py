# 函数嵌套

def f1():
    def f2():
        print('执行了f2了')
    return f2

f3=f1()

print('让f3等于f2的内部f1')
f3()

#返回函数的重要意义：根据传入的不同参数返回不同函数