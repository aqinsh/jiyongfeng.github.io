from cmath import polar, phase
# from cmath import
input_number = input('Please input: ')
m = input_number.split('+')
n = []
x = 0
y = 0
for i in m:
    n.append(i)


if len(n) == 2:
    x = float(n[0])
    y = float(n[1][0])
elif 'j' in n[0]:
    y = float(n[0][0])
else:
    x = float(n[0])

polar_num = polar(complex(x, y))
print(polar_num[0])
print(polar_num[1])
