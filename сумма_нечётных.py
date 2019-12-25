a = int(input("Введите число: "))
if a % 2 == 0:
    a-=1
b = 1
while b != a:
    d = a + b
    b = (b + 2) % a
print(d)
