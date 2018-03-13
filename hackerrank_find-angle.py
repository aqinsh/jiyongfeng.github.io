from math import (sqrt, atan2, degrees)


def mbc_degree(a, b):
    return degrees(atan2(a, b))


x = float(input('Please input a: '))
y = float(input('Please input b: '))
try:
    c = str(round(mbc_degree(x, y)))  # round:四舍五入
    print('the degrees of triangel MBC is {}°'.format(c))
except Exception as e:
    raise e
