# 动态创建类
from types import MethodType

def fn(self, name='world'):
    print('Hello %s' % name)

# 要创建一个class对象，type()函数依次传入3个参数：
#
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。


Hello = type('Hello', (object,), dict(hello=fn))
hello = Hello()
hello.hello('world!')


# dynamic set method
def printStr(self, content):
    print(content)


hello.printStr = MethodType(printStr,hello)
hello.printStr("dynamic set method")

hello.start = "2014.07.01"
hello.printStr(hello.start)