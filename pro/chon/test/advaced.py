def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b
        a, b = b, a+b
        n += 1
    return "done"


g = fib(6)

# for n in g:
#     print(n)

while True:
    try:
        x = next(g)
        print("g =", x)
    except StopIteration as e:
        print("Generator return value:", e.value)
        break


def triangles():
    li = [1]
    while True:
        yield li
        li = li[:]
        li.append(0)
        li = [li[i - 1] + li[i] for i in range(len(li))]


# def triangles():
#     li = [1]
#     while True:
#         old_li = li[:]
#         yield old_li
#         for i in range(1, len(li)):
#             li[i] = old_li[i] + old_li[i - 1]
#         li.append(1)


# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break

print(results)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')


# from collections import Iterator
# print(isinstance((x for x in range(10)), Iterator))

for x in [1, 2, 3, 4, 5]:
    pass

# 等价于
it = iter([1, 2, 3, 4, 5])

while True:
    try:
        v = next(it)
        print("v =",v)
    except StopIteration as e:
        break

print(hex(100))


# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)

def fact(n):
    return face_iter(n, 1)


def face_iter(num, product):
    if num == 1:
        return product
    else:
        return face_iter(num - 1, num * product)


print(fact(4))


def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 6, abs))



