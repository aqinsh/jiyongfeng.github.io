def expanded_form(num):
    s = str(num)
    l = len(s)-1
    n = []
    for i in range(l+1):
        if s[i] != '0':
            n.append(10 ** (l-i)*int(s[i]))

    return ' + '.join(map(str, n))


def find_outlier(integers):
    if integers[0] % 2 == integers[1] % 2:
        flag = integers[0] % 2
        for i in integers:
            if i % 2 != flag:
                return i
    else:
        if integers[0] % 2 == integers[2] % 2:
            return integers[1]
        else:
            return integers[0]


def reverseWords(str):
    return ' '.join(reversed(str.split()))


def tickets(people):
    a = b = 0
    for i in people:
        if i == 25:
            a += 1
        elif i == 50:
            b += 1
            a -= 1
            if a < 0:
                return 'NO'                
        elif i == 100 and b > 0:
            a -= 1
            b -= 1
            if a < 0 :
                return 'NO'                
        elif i == 100 and b == 0:
            a -= 3
            if a < 0:
                return 'NO'                
    return 'Yes'
             

def tickets1(a):
    n25 = n50 = 0
    for e in a:
        if e == 25:
            n25 += 1
            print(n25)
        elif e == 50:
            n25 -= 1
            n50 += 1
            print(n25)
        elif e == 100 and n50 > 0:
            n25 -= 1
            n50 -= 1
        elif e == 100 and n50 == 0:
            n25 -= 3
        if n25 < 0 or n50 < 0:
            return 'NO'
    return 'YES'
p = [50, 25, 25]

print(tickets(p))
print(tickets1(p))