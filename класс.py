from girl import girl
from boy import boy
import random
a = []
m = int(input("Введите кол-во мальчиков: "))
n = int(input("Введите кол-во девочек: "))
for i in range (m):
    q = boy()
    a.append(q)
for i in range (n):
    w = girl()
    a.append(w)
random.shuffle(a)
for i in range (len(a)):
    a[i].workout()
    

