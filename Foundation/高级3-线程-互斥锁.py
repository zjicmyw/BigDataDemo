# 互斥锁：解决资源竞争
import threading

g_num = 0
# 创建锁
lock = threading.Lock()
lock2 = threading.Lock()

islock = True
islock2 = False


def plus1():
    if islock:
        lock.acquire()
    global g_num
    for i in range(1000000):
        if islock2 and not islock:
            lock2.acquire()
        g_num += 1
        if islock2 and not islock:
            lock2.release()
    if islock:
        lock.release()
    print('plus1:', g_num)


def plus2():
    if islock:
        lock.acquire()
    global g_num
    for i in range(1000000):
        if islock2 and not islock:
            lock2.acquire()
        g_num += 1
        if islock2 and not islock:
            lock2.release()
    if islock:
        lock.release()
    print('plus2:', g_num)


if __name__ == '__main__':
    my_thread1 = threading.Thread(target=plus1)
    my_thread2 = threading.Thread(target=plus2)
    my_thread1.start()
    my_thread2.start()

# plus1: 1227357 plus2: 1239789  结果不是 10000000*2
# 加入lock锁后 plus1: 1000000   plus2: 2000000
# 加入lock2锁后 plus2: 1961433  plus1: 2000000
