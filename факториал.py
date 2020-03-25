a = int(input("Введите число: "))
k = 1
for i in range (1, a + 1, 1):
    k = k * i
print (f"{a}! = {k}")