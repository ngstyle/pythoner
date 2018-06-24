from multiprocessing import Process
import os


def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


print('Parent process %s.' % os.getpid())
p = Process(target=run_proc, args=('test',))
print('Child process will start.')
p.start()
p.join()
print('Child process end.')


# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：