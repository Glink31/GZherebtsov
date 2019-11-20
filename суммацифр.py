a = int(input("Введите число: "))
n = 10
b = a - (a // n)
while b > 9:    
    n = n * 10 
    b = a - (a // n)
print(f"{b}")
