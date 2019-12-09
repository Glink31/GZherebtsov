def smth (a):
    if a > 0:
        b = a % 10
        b = b + 1
        if b == 10:
            b = 0
        return smth (a // 10)
a = int(input("Введите число "))
b = smth (a)
print()