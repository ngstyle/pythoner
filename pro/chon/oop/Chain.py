class Chain(object):

    def __init__(self, path=''):
        self.__path = path

    # __getattr__ 妙用
    def __getattr__(self, item):
        if item == 'users':
            return lambda x: Chain('%s/%s/%s' % (self.__path, item, x))
        return Chain('%s/%s' % (self.__path,item))

    def __str__(self):
        return self.__path

    def __call__(self, *args, **kwargs):
        return 'path is %s' % self.__path

    __repr__ = __str__


# chain = Chain().status.user.timeline.list
chain = Chain().users('michael').repos
print(chain)
print(chain())

# 可被调用
print(callable(chain))
