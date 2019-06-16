"""
https://github.com/jackfrued/Python-100-Days/
练手用

CreateDate: 2019-06-12
"""

import math
import os
import time
import random


def area_round(radius):
    """
    计算圆的面积

    Args:
        radius: 圆的半径
    
    Returns:
        圆面积，格式化输出，保留小数点3位
    """
    s = math.pi * (radius ** 2)
    return '{:.3f}'.format(s)


def perimeter_round(radius):
    """
    计算圆的周长
    Version: 0.1
    Author:Steven
    Date: 2019-06-12
    """
    return 2 * math.pi * radius


def checkleapyear(year):
    """
    判断闰年，如是，返回True，否则返回False
    Version: 0.1
    Author:Steven
    Date: 2019-06-12
    """
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def math1(x):
    """
    分段函数求值
            3x - 5	(x > 1)
    f(x) =	x + 2	(-1 <= x <= 1)
            5x + 3	(x < -1)

    Version: 0.1
    Author: Steven
    Date: 2019-06-14
    """
    if x > 1:
        return 3 * x - 5
    elif x >= -1 and x <= 1:
        return x + 2
    else:
        return 5 * x + 3


def sumint(a, b):
    return sum(range(a, b+1))


def narcissistic():
    """
    水仙花数三位数，每位数的幂之和如果等于该数，则该数为水仙花数
    Version: 0.1
    Author: Steven
    Date: 2019-06-14
    """
    for i in range(100, 1000):
        x = list(str(i))
        if int(x[0]) ** 3 + int(x[1]) ** 3 + int(x[2]) ** 3 == i:
            print(i)


def perfect_number(n):
    """
    输出n位数中的完全数，即该数的所有除自身以外的因数之和等于该数

    Args:
        n:数字的位数，比如n=3表示需要找所有从100~999中符合的完全数

    Returns:
        返回符合的所有数字，以列表显示

    """
    total = []
    for x in range(10 ** (n-1), 10 ** n):
        temp = 0
        for i in range(1, x // 2 + 1):
            if x % i == 0:
                temp += i
                # print(temp)
        if temp == x:
            # print(x)
            total.append(x)
    return total


def baijibaiqian():
    """
    百鸡百钱问题求解

    Args:
        None


    Returns:
        返回所有解
    """

    for i in range(100):
        for j in range(100):
            for k in range(100):
                if i + j + k == 100 and 5 * i + 3 * j + k / 3 == 100:
                    print("鸡翁:{:2d}，鸡母:{:2d}，鸡雏:{:2d}".format(i, j, k))


def generate_code(code_len=4):
    """
    生成指定长度的验证码

    Args:
        param code_len: 验证码的长度(默认4个字符)

    Returns: 
        由大小写英文字母和数字构成的随机验证码
    """
    chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    str_lenth = len(chars)
    code = ''
    for _ in range(code_len):
        code += chars[random.randint(0, str_lenth-1)]
    return code


def maxnumber(l):
    """
    返回列表中的最大数值

    Args:
        l:给出列表

    Returns:
        列表中的最大数值
    """

    max_number = l[0]
    for i in l[1:]:
        if i >= max_number:
            max_number = i
    return max_number


def main():
    print(area_round(float(input('Please input the round\'s radius:'))))


if __name__ == "__main__":
    main()
