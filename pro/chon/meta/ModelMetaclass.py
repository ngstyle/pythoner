from pro.chon.meta.Filed import Field


class ModelMetaclass(type):
    # __new__()方法接收到的参数依次是：
    #
    # 当前准备创建的类的对象；
    #
    # 类的名字；
    #
    # 类继承的父类集合；
    #
    # 类的方法属性集合。
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print("Found Model :%s" % name)
        mappings = dict()

        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v

        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)
