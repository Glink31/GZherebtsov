def smth (a):
    if a > 0:
        b = (a % 10 + 1) % 10  
        smth (a // 10)
        print(b,end="")
a = int(input("Введите число "))
smth (a)
print()