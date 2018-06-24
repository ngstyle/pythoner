from pro.chon.meta.ChildField import IntegerField, StringField
from pro.chon.meta.Model import Model


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


user = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
user.save()