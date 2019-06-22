import random

def create_10file():
    filepath = '/Users/jiyongfeng/Desktop/python'
    for i in range(1,11):
        open(filepath+'/'+str(i)+'.txt','w')

def invest(amount,rate,time):
    total_amount = amount
    print('principal amount:{}'.format(amount))
    for i in range(time):
        total_amount *= 1 + rate
        print('year {}:{}'.format(i,total_amount))
    return None

def roll_dice():
    """ 
    骰子游戏
    
    Args:
        n:玩家猜测，1为大，0为小
        
    Returns:
        返回玩家猜测结果，True表示正确，False表示错误
    
    """
    s = input("Big or Small:")
    n = 0
    if s == 'Big':
        n = 1
    elif s == 'Small':
        n = 0
    else:
        roll_dice()
    points = []
    result = ''
    for _ in range(3):
        points.append(random.randint(1,6))
    if (sum(points) >= 11 and n == 1) or (sum(points) < 11 and n == 0):
        result = 'Win'
    else:
        result = 'Lose'
    print('The points are {} You {}!'.format(points,result))



    
    


