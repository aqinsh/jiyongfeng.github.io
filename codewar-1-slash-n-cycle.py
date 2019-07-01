#
# codewar-1-slash-n-cycle.py
# @author Ji Yongfeng
# @https://www.codewars.com/kata/1-slash-n-cycle?utm_source=newsletter&utm_medium=email&utm_campaign=weekly_coding_challenges&utm_term=2019-06-30
""" Let be n an integer prime with 10 e.g. 7.
 1/7 = 0.142857 142857 142857 ....
We see that the decimal part has a cycle: 142857. The length of this cycle is 6. In the same way:
1/11 = 0.09 09 09 .... Cycle length is 2.
Task
Given an integer n(n > 1), the function cycle(n) returns the length of the cycle if n and 10 are coprimes, otherwise returns - 1.
 """
# @created 2019-06-30T18:50:23.000Z+08:00
# @last-modified 2019-06-30T21:28:20.017Z+08:00
#


# 判断1/n的小数循环节点长度
def cycle_length(n):
    length = 1
    while(True):
        if (10**length-1) % n == 0:
            break
        length += 1
    return length


def cycle(n):
    mod = 1 % n
    i = 1
    if n % 2 == 0 or n % 5 == 0:
        return -1
    else:
        k = []
        for _ in range(cycle_length(n)):
            i = (mod * 10) // n
            mod = (mod * 10) % n
            k.append((i))
    return ''.join(str(i) for i in k)


