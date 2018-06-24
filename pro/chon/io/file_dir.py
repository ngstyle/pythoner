import os

print(os.name)
if 'posix' == os.name:
    print('unix or linux')
elif 'nt' == os.name:
    print('windows')

# 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。
print(os.uname())

print('\nenviron:')
# print(os.environ)
print('\nPATH:')
print(os.environ.get('PATH'))
print(os.environ.get('x', 'default'))


# 查看当前目录的绝对路径:
print(os.path.abspath('.'))
# 两个路径合成一个
chon = os.path.join(os.path.abspath('.'), 'chon')
print(chon, 'chon')

os.mkdir(chon)
# os.rmdir(chon)

# 要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
os.path.split('/Users/michael/testdir/file.txt')
# s.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
os.path.splitext('/Users/michael/testdir/file.txt')
# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。


# 对文件重命名:
os.rename('test_read1.py', 'test_read.py')
# 删掉文件:
os.remove('test.txt')
