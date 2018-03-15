n = int(input())
x = []
for i in range(1, n + 1):
    x.append(i)
t = tuple(x)
print(t)
print(hash(t))
