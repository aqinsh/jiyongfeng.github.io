

M1 =list(map(int, input().split()))
M2 = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
score = 0
for i in M2:
    if i in A:
        score += 1
    elif i in B:
        score -=1

print(score)
