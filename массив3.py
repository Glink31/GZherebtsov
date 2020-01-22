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
p = 0
for i in range(1,len(a)):
    if a[i] > a[p]:
        p = i
print(f'наибольшее: {p}. {a[p]}')