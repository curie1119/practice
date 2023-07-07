import random
 
win = defeat = 0
balance = 3
while True:
    user = input('Орёл - 0 или Решка - 1: ')
    if user not in ('01'):
        print('Конец игры.')
        break
 
    pc = random.choice('01')
    if pc == user:
        win += 1
        balance += 1
    else:
        defeat += 1
        balance -= 1
    print(f'Побед: {win}\nПоражений: {defeat}\nБаланс: {balance}')
    if balance <= 0:
        break
