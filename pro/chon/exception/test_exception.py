from functools import reduce
import logging
logging.basicConfig(level=logging.INFO)


def str2num(s):
    return eval(s)


def calc(exp):
    ss = exp.split('+')
    # logging.info("ss = %s" % str(ss[0]))
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()