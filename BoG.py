a = int(input())
if a < 0:
    print("incorrect imput") 
b = int(input())
if b < 0:
    print("incorrect imput")
pos = False
i = 0
while i <= a and i <= b:
    if (a%3 == 0 and b%3 == 0) or ((a-i)%3 == 0 and (b-i)%3 == 0):
        pos = True
        break
    i += 1
if pos:
    i = 0
    found = False
    while (i <= a and i <= b):
        if (a%3 == 0 and b%3 == 0) or ((a-i)%3 == 0 and (b-i)%3 == 0):
            if a%3 == 0:
                print(f"{a//3} 0 {b//3}")
                break
            elif (a-i)%3 == 0:
                print(f"{a//3} {i} {b//3}")
                break
        i+=1
else:
    print("-1")
    