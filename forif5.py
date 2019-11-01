n = int(input("Введите n "))
for i in range (n):
    for j in range(n):
        if (i <= j and i < n-j) or (i >= j and i >= 0.5*(n-j/2)):
            print("*",end="")
        else:
            print(".",end="")
    print()
            