a = []
for i in range (5):
    a.append (int(input('введите оценку ученика: ')))
bad = False
exc = True
for i in range(len(a)):
    if a[i] <= 2:
        bad = True
    if a[i] < 5:
        exc = False
if exc:
    print('ученик - отличник')
elif bad:
    print('ученик - двоечник')
else:
    print('ученик - обычный')