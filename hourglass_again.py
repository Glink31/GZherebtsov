def hour (n,m):
    for i in range (n, 0, -2):
        for k in range (n//2-i//2+m):
            print(" ",end="")
        for j in range (i):
            print(f"*",end="")
        print()
    for i in range (3, n+1, 2):
        for k in range (n//2-i//2+m):
            print(" ",end="")
        for j in range (i):
            print(f"*",end="")
        print()
    return()
n = int(input("Введите число: "))
m = 0
for i in range (n, 0, -2):
    m = n//2 - i//2
    a = hour (i,m)
for i in range (3, n+1, 2):
    m = n//2 - i//2
    a = hour (i,m)