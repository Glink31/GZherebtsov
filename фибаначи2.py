def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)
a = int(input("Введите номер в ряде фибаначи: "))
b = fib(a)
print(f"В ряде фибаначи на месте {a} стоит число {b}")