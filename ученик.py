a = []
for i in range (5):
    a.append (int(input('введите оценку ученика: ')))
b = False
c = 0
for i in range(len(a)):
    if a[i] <= 2:
        print('ученик - двоечник')
        b = True
        break
    if a[i] == 5:
        c += 1
if c == len(a):
    print('ученик - отличник')
    b = True
if not b:
    print('ученик - обычный')