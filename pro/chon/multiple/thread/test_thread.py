import threading,time

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


print('Thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='loopThread')
t.start()
t.join()
print('Thread %s ended.' % threading.current_thread().name)