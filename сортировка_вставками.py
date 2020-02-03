a = []
b = int(input('Введите размер массива: '))
for i in range (b):
    a.append(int(input('Введите число массива: ')))
print()
for i in range (1,len(a)):
    while a[i] < a[i-1] and i != 0:
        a[i], a[i-1] = a[i-1], a[i]
        i -= 1
for i,x in enumerate(a):
    print(f'{i}. {x}')