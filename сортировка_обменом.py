a = []
b = int(input('Введите размер массива: '))
for i in range (b):
    a.append(int(input("Введите число массива: ")))
print()
swap = True
while swap:
    swap = False
    for i in range (1,len(a)):
        if a[i-1] > a[i]:
            a[i] = a[i] + a[i-1]
            a[i-1] = a [i] - a[i-1]
            a[i] = a[i] - a[i-1]
            swap = True
for i,x in enumerate(a):
    print (f'{i}. {x}')