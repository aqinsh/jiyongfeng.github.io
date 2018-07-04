import timeit


def array_diff(a, b):
    s = [i for i in a if i not in b]
    return s


def count_smileys(arr):
    Smile_face1 = [':', ';']
    Smile_face2 = ['-', '~']
    Smile_face3 = [')', 'D']
    total = 0
    for i in arr:
        if len(i) == 3:
            if (i[0] in Smile_face1 and i[1] in Smile_face2 and
                    i[2] in Smile_face3):
                total += 1
        elif len(i) == 2:
            if i[0] in Smile_face1 and i[1] in Smile_face3:
                total += 1
    return total


def find_even_index(arr):
    for i in range(len(arr)):
        sum1 = sum(arr[:i])
        sum2 = sum(arr[(i+1):])
        if sum1 == sum2:
            return i


def check_three_and_two(array):
    return len(set(array)) == 2 and array.count(array[0]) in [2, 3]


def pig_it(text):
    s = []
    for i in text.split(' '):
        if i.isalnum() and i[-2:] != 'ay':
            s.append(i[1:] + i[0] + 'ay')
        else:
            s.append(i)
    return ' '.join(s)


# def decodeMorse(morse_code):
#    s = morse_code.split('   ')
#    r = []
#    for i in s:
#        r.append(''.join(n.replace(n,MORSE_CODE[n]) for n in i.split()))
#    return ' '.join(r)


def primeFactors(n):
    i = 2
    r = ''
    while n != 1:
        k = 0
        while n % i == 0:
            n = n / i
            k += 1
        if k == 1:
            r = r + '(' + str(i) + ')'
        elif k == 0:
            pass
        else:
            r = r + '(' + str(i) + '**' + str(k) + ')'
        i += 1

    return r


def scramble(s1, s2):
    # your code here
    s = [i for i in s1]
    result = True
    for i in s2:
        if i in s:
            s.remove(i)
        else:
            result = False
    return result


def next_bigger(n):
    if n < 10:
        return -1
    else:
        if str(n)[-1] == str(n)[-2]:
            return -1
        else:
            return int(str(n)[:-2] + str(n)[-1]+str(n)[-2])


def to_camel_case(text):
    s = text.split('_')
    r = [s[0]]
    for i in range(1, len(s)):
        r.append(s[i].title())
    return ''.join(r)


def removNb(n):
    total = n*(n+1)/2
    sol = []
    for a in range(1, n+1):
        b = (total-a)/(a+1.0)
        if b.is_integer() and b <= n:
            sol.append((a, int(b)))
    return sol


def removNb2(n):
    total = sum(range(1, n+1))
    s = []
    for i in range(1, n+1):
        mod_j = (total - i) % (i + 1)
        j = (total - i) // (i + 1)
        if mod_j == 0 and j < n:
            s.append((i, j))
    return s


def rgb(r, g, b):
    # return(hex(r)+hex(g)+hex(b))
    def check_rgb(n):
        if n >= 255 :
            return 255
        elif n <= 0:
            return 0
        else:
            return n
    return ''.join('{:02X}'.format(check_rgb(i)) for i in (r,g,b) )


def fibonacci(n):
    x = [0, 1]
    if n in x:
        return n
    else:
        for i in range(n - 2):
            x.append(x[-2] + x[-1])
        return x[-1]


def fibonacci1(n):
    if n in [0, 1]:
        return n
    else:
        return fibonacci1(n-1) + fibonacci1(n-2)


def prime_number(n):
    r =True
    if n < 2:
        r = False
    else:
        # for i in [j for j in range(2, int(n ** 0.5)+1) if j % 2 != 0]:
        for i in range(2,int(n ** 0.5)+1):
            if n % i == 0:
                r = False
    return r 

for i in range(10):
    start = timeit.default_timer()
    print(prime_number(107))
    stop = timeit.default_timer()
    x = 0.0
    x += stop - start
    print('Program Excuted in {:.5f}'.format(stop - start))
print('The average program excute time is {:.5f}'.format(x/10))
