from random import randint
a = []
b = int(input("Введите размер массива: "))
for i in range (b):
    c = randint(-5,10)
    a.append(c)
c = int(input('Введите число'))
for i,x in enumerate(a):
    print (f'{i}. {x}')
    if c == x:
        print(i)