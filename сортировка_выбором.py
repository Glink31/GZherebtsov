a = []
b = int(input('Введите размер массива: '))
for i in range (b):
    a.append(int(input('Введите число массива: ')))
print()
for i in range (len(a)):
    for j in range (len(a)):
        if a[i] < a[j]:
            a[i] = a[i] + a[j]
            a[j] = a[i] - a[j]
            a[i] = a[i] - a[j]
for i,x in enumerate(a):
    print(f'{i}. {x}')