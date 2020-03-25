a = str(input('Введите строку: '))
f = str(input('Введите искомый символ: '))
Found = False
for i,x in enumerate(a):
    if f == x:
        print(i)
        Found = True
        break
if not Found:
    print('Такого символа нет ')