def fact (a):
    k = 1
    for i in range (1, a + 1):
        k = k * i
    return k
n = int(input("Введите число n: "))
m = int(input("Введите число m: "))
q = fact(n)

R = q
print (f"{R}")