
""" 珠心算测验 """
n = int(input())
l = input().split()
l.sort()
tip = []
sum = 0
new = [(x, y, z) for x in l for y in l for z in l if int(x) + int(y) == int(z) and int(x) < int(y)]
tip.append(new[0][2])
for i in new:
    if tip.count(i[2]) == 0:
        tip.append(i[2])
print(len(tip))
