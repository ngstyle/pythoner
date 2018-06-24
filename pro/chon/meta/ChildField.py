from pro.chon.meta.Filed import Field


class IntegerField(Field):

    def __init__(self, name):
        Field.__init__(self, name, 'bigint')


class StringField(Field):

    def __init__(self, name):
        Field.__init__(self, name, "varchar(100)")
