import types


class Person(object):

    def __init__(self, gender):
        self.__gender = gender

    def name1(self):
        print("Person")


class Zhiye(object):

    def name1(self):
        print("zhiye")


class Student(Person,Zhiye):
    label = "Student"
    count = 0
    __slots__ = ('__name', '__age')  # 限制实例的属性

    def __init__(self, gender, name, age):
        # Person.__init__(self, gender)
        super().__init__(gender)
        self.__name = name
        self.__age = age
        Student.count += 1

    def print(self):
        print("name: %s, age: %d" % (self.__name, self.__age))

    def __len__(self):
        return self.__age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            raise ValueError("name must be str!")
        self.__name = name

    def __str__(self):
        return 'Student object(name = %s)' % self.name

    def printSuperName(self):
        Person.name1(self)

    __repr__ = __str__


if Student.count != 0:
    print('测试失败!')
else:
    bart = Student("男", 'Bart', 10)
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student("男", 'Bart', 10)
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')


student = Student("男","nohc", 27)
student.print()


def fn():
    pass


print(isinstance(fn, types.FunctionType))
print(isinstance(abs, types.BuiltinFunctionType))
print(isinstance(lambda x: x, types.LambdaType))

print((isinstance((x + 1 for x in range(0, 10)), types.GeneratorType)))

print(dir(student))

# len方法,实际调用的对象的__len__方法
print(len(student))

# hasattr getattr setattr
hasattr(student, "score")
getattr(student, "score", 82)
# setattr(student, "score", 77)


print(Student.label)
Student.label = "freedom"
print(student.label)
# del student.label
# print(student.label)

ss = Student("男", "chon", 27)
print(ss)
print(ss.name)

ss.printSuperName()