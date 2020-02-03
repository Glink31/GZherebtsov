a = []
b = int(input('Введите размер массива: '))
for i in range (b):
    a.append(int(input('Введите число массива: ')))
print()
for i in range (len(a)-1):
    c = i
    for j in range (i,len(a)):
        if a[c] > a[j]:
            c = j
    if i != c:
        a[i], a[c] = a[c], a[i]
for i,x in enumerate(a):
    print(f'{i}. {x}')