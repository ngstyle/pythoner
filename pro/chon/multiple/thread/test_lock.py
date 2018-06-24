# 多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。
# Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。


import threading, time, random

balance = 0
# 创建一个锁就是通过threading.Lock()来实现
lock = threading.Lock()


def calc(param):
    global balance
    balance = balance + param
    balance = balance - param


def run_thread(param):
    lock.acquire()
    try:
        for i in range(1000000):
            calc(param)
    finally:
        lock.release()


t1 = threading.Thread(target=run_thread, args=(3, ))
t2 = threading.Thread(target=run_thread, args=(10, ))
t1.start()
t2.start()
t1.join()
t2.join()
print('balance = %d' % balance)
