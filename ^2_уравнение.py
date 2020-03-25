import math
a = int(input("Введите значение a "))
b = int(input("Введите значение b "))
c = int(input("Введите значение c "))
D = b*b - 4*a*c
if (a == 0) and (b == 0) and (c == 0):
    print(f"верно при любом x")
elif (a == 0) and (b == 0):
    print(f"корней нет") 
elif (a == 0):
    x0 = -c/b
    print(f"x0={x0}") 
elif D > 0:
    x1 = (-b + math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D))/(2*a)
    print(f"x1={x1} ; x2={x2}")
elif D == 0:
    x0 = (-b)/(2*a)
    print(f"x0={x0}")
else:
    print(f"корней нет")
