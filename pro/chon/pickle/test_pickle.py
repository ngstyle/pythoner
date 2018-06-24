import pickle
import os
import json

d = dict(name='Bob', age=21, score=88)
# print(pickle.dumps(d))

# 把对象序列化到文件
# with open(os.path.join(os.path.abspath('.'), 'test.txt'), 'wb+') as f:
    # f.write(bytes.decode(pickle.dumps(d)))
    # pickle.dump(d, f)

# 从文件中恢复出对象
# with open(os.path.join(os.path.abspath('.'), 'test.txt'), 'rb+') as ff:
#     dd = pickle.load(ff)
#     print(dd.get('name'))

# os.remove('./test.txt')

print(json.dumps(d))

with open(os.path.join(os.path.abspath('.'), 'test.txt'), 'w+') as f:
    json.dump(d, f)
    print(f.read())


class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 88)
print(json.dumps(s, default=lambda obj: obj.__dict__))


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))