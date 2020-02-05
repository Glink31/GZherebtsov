a = []
b = int(input('Введите размер массива: '))
for i in range (b):
    c = int(input('Введите число в массив: '))
    a.append(c)
swap = True
while swap:
    swap = False
    for i in range (1,len(a)):
        if a[i-1] > a[i]:
            a[i], a[i-1] = a[i-1], a[i]
            swap = True
for i,x in enumerate(a):
    print(f'{i}. {x}')
print()
e1 = 0
e2 = len(a)
f = int(input('Введите искомое число: ')) 
drop = False
while not drop and e1 < e2:
    if f == a[e2//2]:
        print(e2//2)
        drop = True
    elif f > a[e2//2]:
        e1 += e2//2
    elif f < a[e2//2]:
        e2 -= e2//2
if not drop:
    print('Такого числа нет')