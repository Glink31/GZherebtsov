from random import randint
n = int(input('Введите количество команд: '))
m = int(input('Введите количество соревнований: '))
a = []
b = []
for i in range (n):
    y = 0
    a.append ([])
    print(f'{i} команда ',end='')
    for j in range (m):
        c = randint(0,10)
        print(f'{c} ',end='')
        y = y+c
    print()
    a[i].append(i)
    a[i].append(y)
z=-1
b.append(0)
b.append(0)
for i in range (len(a)):
    b[0] = 0
    b[1] = 0
    for k in range (len(a)):
        if a[k][1] > b[1]:
            b[0] = a[k][0]
            b[1] = a[k][1]
            z = k
    print(f'{i+1} место- {b[0]} команда, {b[1]}')
    del a[z]