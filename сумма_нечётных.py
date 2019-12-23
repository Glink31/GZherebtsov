a = int(input("Введите число: "))
b = 1
d = 0
if a % 2 == 1:
    d = a
while b != 0:
    if b % 2 == 1:
        d = d + b
    b = (b + 1) % a
print (d)