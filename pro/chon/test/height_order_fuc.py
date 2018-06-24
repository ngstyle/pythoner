
print(list(map(lambda x: x * x, [1, 2, 3])))


from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(ch):
    return DIGITS[ch]


def str2int(s):
    return reduce(lambda x, y: x*10+y, map(char2num, s))


print(str2int('134345'))


def str2float(s):
    ss = str(s)
    index = str(s).index(".") - len(s) + 1
    ss = ss.replace(".", "")
    return reduce(lambda x, y: x * 10 + y, map(char2num, ss)) * pow(10, index)


print(str2float('0.113434534'))


def createCounter():
    def gen():
        n = 0
        while True:
            n += 1
            yield n

    # gen() 方法调用返回的是一个generator, 是一个Iterator
    g = gen()

    def counter():
        return next(g)
    return counter

# def createCounter():
#     n = 0
#
#     def counter():
#         nonlocal n      # nonlocal 是什么鬼？
#         n = n + 1
#         return n
#     return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


# def log(func):
#     def wrapper(*args, **kw):
#         print("call function name", func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
#
# @log
# def now():
#     return "2018-06-03 22:28:10"
#
#
# print(now())

import functools


def log(text):
    def decorator(func):
        @functools.wraps(func)      # now.__name__ 还是now
        def wrapper(*args, **kw):
            print("call name %s, param %s" % (func.__name__, text))
            return func(*args, **kw)
        return wrapper
    return decorator


@log("execute")
def now():
    return "2018-06-03 23:17:41"


print(now())
print(now.__name__)
