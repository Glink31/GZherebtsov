from random import randint
n = int(input('Введите количество команд: '))
m = int(input('Введите количество соревнований: '))
a = []
p = 0
for i in range (n):
    y = 0
    a.append ([])
    print(f'{i}. ',end='')
    for j in range (m):
        c = randint(0,10)
        #a.append(a.append(c))
        a[-1].append(c)
        print(f'{c} ',end='')
        y += c
    if y > p:
        p = y
        z = i
    print()
print(f'победитель {z}')
print(a)