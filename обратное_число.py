def rev (a):
    b = a % 10
    return b    
a = int(input("Введите число: "))
while a > 0:
    b = rev(a)
    print (b,end="")
    a = a // 10
print()