# https://docs.python.org/3/library/functions.html#open

with open('./test.txt', 'a') as f:
    print(f.write('\nnew line'))