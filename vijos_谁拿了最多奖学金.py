def jiangjin(name, score_1, score_2, is_ganbu, is_xibu, lunwen):
    total = 0
    if score_1 > 80 and lunwen > 0:
        total += 8000
    if score_1 > 85 and score_2 > 80:
        total += 4000
    if score_1 > 90:
        total += 2000
    if score_1 > 85 and is_xibu == 'Y':
        total += 1000
    if score_2 > 80 and is_ganbu == 'Y':
        total += 850
    return total


names = []
score_1 = []
score_2 = []
is_ganbu = []
is_xibu = []
lunwen = []
jiang_jin = []

scores = []
for i in range(int(input())):
    x = input().split()
    names.append(x[0])
    score_1.append(int(x[1]))
    score_2.append(int(x[2]))
    is_ganbu.append(x[3])
    is_xibu.append(x[4])
    lunwen.append(int(x[5]))
    jiang_jin.append(
        jiangjin(x[0], int(x[1]), int(x[2]), x[3], x[4], int(x[5])))

top = max(jiang_jin)
top_name = names[jiang_jin.index(top)]
totaljiangjin = 0
for i in jiang_jin:
    totaljiangjin += i

print(top_name)
print(top)
print(totaljiangjin)
