def sum (a): 
    if a == 1:
        return 1
    return sum (a-2) + a
a = int(input("Введите число: "))
if a % 2 == 0:
    a -= 1
c = sum(a)
print (c)