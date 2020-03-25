def rev (a):
    if a > 0:
        b = a % 10
        print (b,end="")
        return rev (a // 10)
a = int(input("Введите число: "))
b = rev (a)
print()