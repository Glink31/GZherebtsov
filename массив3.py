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
d = c-1
for i,x in enumerate(a):
    if x > d:
        d = x
        p = i
print(p)