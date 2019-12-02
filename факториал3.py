def fact (n):
    if n == 0:
        return 1
    return fact(n-1) * n
a = int(input("Введите число: "))
b = fact (a)
print (f"факториал числа {a} - {b}")