import random

print('game start ----')
score = random.randint(1, 10)
temp = 0
while int(temp) != score:
    temp = input('请输入成绩:')
    if int(temp) == score:
        print('is right')
    else:
        print('is wrong')
print('game over')
