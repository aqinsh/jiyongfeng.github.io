result = []
score = []
wins = 0
loss = 0

while True:
    x = input()
    if 'E' not in x:
        result.append(x)
    else:
        result.append(x[:x.find('E')])
        break
for i in result:
    for j in i:
        score.append(j)

#print(score)

for i in score:
    if i == 'W':
        wins += 1
    else:
        loss += 1
    if wins >= 11 and abs(wins - loss) > 1:
        print('{}:{}'.format(wins, loss))
        wins = loss = 0
    elif loss == 11 and abs(wins - loss) > 1:
        print('{}:{}'.format(wins, loss))
        wins = loss = 0
    elif wins >= 10 and loss >= 10 and abs(wins - loss) == 2:
        print('{}:{}'.format(wins, loss))
        wins = loss = 0

print('{}:{}\n'.format(wins, loss))

wins = 0
loss = 0

for i in score:
    if i == 'W':
        wins += 1
    else:
        loss += 1
    if wins >= 21 and abs(wins - loss) > 1:
        print('{}:{}'.format(wins, loss))
        wins = loss = 0
    elif loss == 21 and abs(wins - loss) > 1:
        print('{}:{}'.format(wins, loss))
        wins = loss = 0
    elif wins >= 20 and loss >= 20 and abs(wins - loss) == 2:
        print('{}:{}'.format(wins, loss))
        wins = loss = 0

print('{}:{}'.format(wins, loss),end = '')
