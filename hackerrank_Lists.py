n = int(input())
y = []
for i in range(n):
    s = input().split()
    for i in range(1, len(s)):
        s[i] = int(s[i])
    if s[0] == 'append':
        y.append(s[1])
    elif s[0] == 'extend':
        y.extend(s[1:])
    elif s[0] == 'insert':
        y.insert(s[1], s[2])
    elif s[0] == 'remove':
        y.remove(s[1])
    elif s[0] == 'pop':
        y.pop()
    elif s[0] == 'index':
        print(y.index(s[1]))
    elif s[0] == 'count':
        print(y.count(s[1]))
    elif s[0] == 'reverse':
        y.reverse()
    elif s[0] == 'print':
        print(y)
    elif s[0] == 'sort':
        y.sort()
