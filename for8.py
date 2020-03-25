n = int(input ("Введите число n "))
for i in range (n, 0, -1):
    for l in range (i):
        print(f"*",end="")
    print()
for k in range (2, n + 1):
    for j in range (k):
        print (f"*",end="")
    print()

