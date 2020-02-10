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
e2 = len(a)-1
h = len(a)//2
f = int(input('Введите искомое число: '))
found = False 
while e1!=e2 and not found:
    if a[h] == f:
        print(f'число найдено под номером {h}')
        found = True
    elif a[h] > f:
        e2 = h-1
        h = h-(e2-e1)-1 
    elif a[h] < f:
        e1 = h+1
        h = h+(e2-e1)+1
if not found:
    print('такого числа нет')