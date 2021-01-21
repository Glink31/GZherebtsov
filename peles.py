a = []
n = int(input('Imput the number of students: '))
for i in range (n):
    a.append(int(input(f'Imput the height of student {i+1}: ')))
moved = []
k = 0
for i in range (len(a)-1):
    j = i
    for b in range (i,len(a)):
        if a[j] > a[b]:
            j = b
    if len(moved) > 0:
        used = False
        for b in range (len(moved)):
            if i == moved[b] or j == moved[b]:
                used = True
        if i != j and (not used):
            moved.append(i)
            moved.append(j)
            a[i], a[j] = a[j], a[i]
            k += 1
    else:
        if i != j:
            moved.append(i)
            moved.append(j)
            a[i], a[j] = a[j], a[i]
            k += 1
possible = True
for i in range (1,len(a)):
    if a[i-1] > a[i]:
        possible = False
if possible:
    print("Yes")
    print(k)
    for i in range (len(moved)-1,0,-2):
        print(f"{moved[i]+1} ",end="")
        print(moved[i-1]+1)
else:
    print("No")