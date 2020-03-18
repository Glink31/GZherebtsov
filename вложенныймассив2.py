from random import randint
n = int(input('Введите количество команд: '))
m = int(input('Введите количество соревнований: '))
a = []
b = []
for i in range (n):
    y = 0
    a.append ([])
    b.append ([])
    for j in range (m):
        c = randint(0,10)
        a[i].append(c)
        y = y+c
    b[i].append(i)
    b[i].append(y)
for i in range (n):
    maxs = 0
    for k in range (1,len(b)):
        if b[i][k]>b[i][k-1]:
            maxs 
    print(f'{i+1} место- {b[maxs][0]} команда, {b[maxs][1]}')
    del b[maxs]