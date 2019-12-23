def sum (a):
    b = (a + 1) % a
    if b != 0:
        if b % 2 == 1:
            if a % 2 == 1:
                c = a + sum(b)
            else:
                c = b + sum (b)
        return c
a = int(input("Введите число: "))
c = sum(a)
print (c)