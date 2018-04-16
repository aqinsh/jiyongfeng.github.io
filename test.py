import math
def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False

x = int(input())
print(x)
y  = []
for i in range(2,int(x / 2)):
    if x % i == 0:
        y.append(i)
print(y)

for s in y:
    test = is_prime(s)
    if test:
        print(s)