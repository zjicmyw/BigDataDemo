# python是模拟多线程（伪）

# threading.Thread()创建
# threading.currentThread(): 返回当前的线程变量。
# threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
# threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
# 除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:
# run(): 用以表示线程活动的方法。
# start():启动线程活动。
# join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
# isAlive(): 返回线程是否活动的。
# getName(): 返回线程名。
# setName(): 设置线程名。
import threading
import time


def show1():
    print(threading.currentThread())
    for i in range(10):
        print('AA')


def show2(n1,n2):
    print(threading.currentThread())
    for i in range(n1,n2):
        print('BB')

def show3():
    print(threading.currentThread())
    while True:
        print('CC')

if __name__ == '__main__':
    print(threading.currentThread())

    # 创建子线程
    my_thread1 = threading.Thread(target=show1)
    my_thread2 = threading.Thread(target=show2, args=(2,12))
    my_thread3 = threading.Thread(target=show3)
    # 设置 setDaemon(True) 主线程结束时候，子线程是否自动结束（是）。
    # 设置需要在启动前
    my_thread3.setDaemon(True)
    # 启动子线程
    my_thread1.start()
    my_thread2.start()
    my_thread3.start()
    print('主线程结束')
