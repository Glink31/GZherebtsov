n = int(input("Введите n "))
for i in range (n):
    for j in range(n):
        if i == (n-j-1) or i == j:
            print("*",end="")
        else:
            print(".",end="")
    print()