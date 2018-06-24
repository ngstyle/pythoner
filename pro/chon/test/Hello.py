from collections import Iterable

zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"

# 切片
print(zodiac[0:4])

# 连接
print(zodiac[1] + zodiac[2:8])

# 相乘
print(zodiac[-1] * 3)

# 记录生肖，根据年份来判断生肖

zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
               u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
               (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

# (month, day) = (16, 12)
# zodiac_day = list(filter(lambda x: x <= (month, day), zodiac_days))
# zodiac_len = len(zodiac_day) % 12
# print(zodiac_name[zodiac_len])

print('天蝎座' in zodiac_name)
print('🐶' not in zodiac_name)


print('type = ', type(8))


# while True:
#     month = int(input("请输入月份"))
#     if (month > 12) or (month < 1):
#         print("月份输入不正确")
#         continue
#
#     day = int(input("请输入日期"))
#     if day < 1:
#         print("日期输入不正确")
#         continue
#
#     if month == 2 and day > 28:
#         print("2月只有28天诶")
#     elif month <= 7 and month%2 == 1 and day > 31:
#         print("这个月只有31天诶")
#     elif month <= 7 and month%2 == 0 and day > 30:
#         print("这个月只有30天诶")
#     elif month >= 8 and month % 2 == 1 and day > 30:
#         print("这个月只有30天诶")
#     elif month >= 8 and month % 2 == 0 and day > 31:
#         print("这个月只有31天诶")
#     else:
#         zodiac_day = list(filter(lambda x: x <= (month, day), zodiac_days))
#         zodiac_len = len(zodiac_day) % 12
#         print("%d 月 %d 日出生的是 %s" % (month, day, zodiac_name[zodiac_len]))
#     print("")

# for year in range(2000, 2019):
#     print("%s 年是 %s 年" % (year, zodiac[year % 12]))
#
#
# print((1, 12) > (2, 1))

dic = {'boy': "chon", 'girl': "hy"}
s = {1}
s.add((1, 2))
s.add(1)

l = [1, 3, 4]
l.remove(3)
l.append(1)

print(l)
print(s)

alist = [i*i for i in range(0, 11) if i % 2 == 0]
print(alist)


print([m+n for m in range(1, 11) if m % 2 == 1 for n in range(1, 11) if n % 2 == 0])


data = {"nohc": "nice", "hy": "beauty", "gg": "baby"}

# 迭代
for k, v in data.items():
    print(k + " = " + v)

# isinstance 判断类型
print(isinstance("nohc", (str, int)))


print(isinstance("nohc", Iterable))


def findMinAndMax(L):
    if len(L) == 0:
        return None, None
    elif len(L) == 1:
        return L[0], L[0]

    L.sort()
    min = L[0]
    max = L[-1]
    return min, max


if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')


for x, y in [(1, 3), (3, 5)]:
    print("x =", x, ",y =", y)


import os

print([d for d in os.listdir(".") if d.startswith("H")])


L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [s.lower() for s in L1 if isinstance(s, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

# generator
g = (x*x for x in range(0, 11))
for value in g:
    print(value)


a, b = (3, 4)
a, b = b, a+b
print("a =",a,"b =",b)

