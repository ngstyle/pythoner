import threading
# ThreadLocal对象
thread_local = threading.local()


def process_student():
    # 获取当前线程关联的student:
    std = thread_local.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    thread_local.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('nohc', ), name='nohc-thread')
t2 = threading.Thread(target=process_thread, args=('chon', ), name='chon-thread')
t1.start()
t2.start()
