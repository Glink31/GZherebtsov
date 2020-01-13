a = []
b = int(input("Введите размер массива: "))
for i in range (b):
    a.append(int(input(f"Введите {i} число массива: ")))
c = 0
for i,x in enumerate (a):
    print (f'{i}. {x}')
    c += x
print (c)