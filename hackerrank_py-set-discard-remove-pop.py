n = int(input())
s = set(map(int, input().split()))
m = int(input())
total = 0
while m > 0:
    command = input()
    if command.startswith('pop'):
        s.pop()
    elif command.startswith('remove'):
        l = command.split()
        s.remove(int(l[1]))
    elif command.startswith('discard'):
        l = command.split()
        s.discard(int(l[1]))
    m -= 1
for i in s:
    total += i
print(total)

