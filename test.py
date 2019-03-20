nums = list(map(int, input().split()))
target = int(input())
total,l = [],[]
for i,j in enumerate(nums):
    if i + j == target:
        print(i,j)
        l.append(i)
        l.append(j)
        total.append(l)
print(total)
