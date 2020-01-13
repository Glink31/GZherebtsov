a = int(input("Введите число: "))
b = 1
if a % 2 == 0:
    a-=1
d = a
while b != a:
    d = d + b
    b = b + 2
print(d)