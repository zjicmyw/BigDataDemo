# __all__：限制import * 开放的内容
__all__=['show']


def show():
    # __name__=='__main__': 自己运行，和引用运行执行不同
    if __name__=='__main__':
        print('在当前模块执行')
    else:
        print('在引用模块执行')
show()