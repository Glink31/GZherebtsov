n = int(input ("Введите нечётное число n "))
while n%2 == 0:
    print("ввод некорректен")
    n = int(input("Введите нечётное число n "))
for i in range (n, 0, -2):
    for k in range (n//2-i//2):
        print(" ",end="")
    for j in range (i):
        print(f"*",end="")
    print()
for i in range (3, n+1, 2):
    for k in range (n//2-i//2):
        print(" ",end="")
    for j in range (i):
        print(f"*",end="")
    print()