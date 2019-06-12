"""
https://github.com/jackfrued/Python-100-Days/
练手用
CreateDate: 2019-06-12
import math


def area_round(radius):
    """
    计算圆的面积
    Version: 0.1
    Author:Steven
    Date: 2019-06-12
     """
    return math.pi * (radius ** 2)


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
