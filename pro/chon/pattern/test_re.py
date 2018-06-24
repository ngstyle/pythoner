import re

# A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。
#
# ^表示行的开头，^\d表示必须以数字开头。
#
# $表示行的结束，\d$表示必须以数字结束。

# 用*表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符：

# print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))

print(re.match(r'^\d{3}-\d{3,8}$', '010-12345'))

# 邮箱
print(re.match(r'[0-9a-zA-Z_]{3,}@[0-9a-zA-Z]+', 'chon_den@sina.com'))



# 正则表达的字符串分割
# 如果用户输入了一组标签，下次记得用正则表达式来把不规范的输入转化成正确的数组
text = 'a b  c d'
print(text.split(' '))
print(re.split(r'\s+', text))

text = 'a , , b ; c , d e'
print(re.split(r'[\s,;]+', text))


# 分组
t = '17:55:19'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())


# 贪婪匹配
text = '102300'
print(re.match(r'^(\d+)(0*)$', text).groups())

# 非贪婪匹配
print(re.match(r'^(\d+?)(0*)$', text).groups())

re_phone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_phone.match('010-12345').groups())
