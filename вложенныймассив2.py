from random import randint
n = int(input('Введите количество команд: '))
m = int(input('Введите количество соревнований: '))
a = []
b = []
p = 0
for i in range (n):
    y = 0
    a.append ([])
    b.append([])
    print(f'{i}. ',end='')
    for j in range (m):
        c = randint(0,10)
        a[i].append(c)
        y = y+c
    b[i].append(i)
    b[i].append(y)
