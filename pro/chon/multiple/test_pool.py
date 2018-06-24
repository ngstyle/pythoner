from multiprocessing import Pool
import os,time,random


def muck_task(name):
    print('run task (%s) in %s' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 5)
    end = time.time()
    print('task %s run %0.2f seconds.' % (name, (end - start)))


# 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。

print('Parent Process run, pid = %s' % os.getpid())
pool = Pool(4)
for i in range(5):
    pool.apply_async(muck_task, args=(i,))
print('waiting for all tasks done...')
pool.close()
pool.join()
print('All subProcess done.')