# 在内存中读写字符串

from io import StringIO

si = StringIO()
si.write('Hello ')
si.write('World ')
si.write('!')
print(si.getvalue())

f = StringIO('How\nAre\nYou|')
while True:
    line = f.readline()
    if line == '':
        break

    print(type(line), line.strip())
    # print(line)
    # print(line.strip())

from io import BytesIO

bi = BytesIO()
# bi.write('中国'.encode('UTF-8'))
bi.write(bytes('中国', encoding='UTF-8'))
print(bi.getvalue())


b = BytesIO(b'\xe4\xb8\xad\xe5\x9b\xbd')
print(b.read().decode())
