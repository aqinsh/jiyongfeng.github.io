number = 12305
l = list(int(i) for i in str(number) if int(i) != 0)
ji = 1
for i in l:
    ji *= i
print(l, ji)
