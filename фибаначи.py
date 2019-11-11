a = int(input("Введите число: "))
b = 1
c = 1
for i in range(2, a):
    b = b + c
    c = b - c
print(f"В ряде Фибаначи на позиции {a} стоит число {b}")
