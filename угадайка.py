from random import randint
a = randint(1, 100)
b = int(input("введите число от 1 до 100: "))
k = 1
while b != a:
    if b > a:
        print("введённое число больше")
    else:
        print("введённое число меньше")
    k = k + 1
    b = int(input("введите число от 1 до 100: "))
print (f"Верно, попыток затрачено {k}")