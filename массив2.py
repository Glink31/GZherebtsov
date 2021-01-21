def mass (a):
    for i,x in enumerate(a):
        print (f'{i}. {x}')
from random import randint
a = []
b = int(input("Введите размер массива: "))
for i in range (b):
    c = randint(-5,10)
    a.append(c)
mass (a)
found = False
c = int(input('Введите число: '))
for i,x in enumerate(a):
    if c == x:
        print(i)
        found = True
        break
if not found:
    print('такого числа нет')
d = int(input("f"))
a.remove(d)
mass (a)