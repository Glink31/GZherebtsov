def smth (a):
    b = a % 10 + 1
    if a > 0 and b == 10:
        b = 0
    smth (a // 10)
    print (b,end="")    
a = int(input("Введите число "))
smth (a)
print()