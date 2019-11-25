a = int(input("Введите число: "))
b = 10 
d = 0
while a > 0:
    b = a % 10
    a = a // 10
    d = d + b
print(f"{d}")