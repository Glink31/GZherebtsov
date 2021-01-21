from rubles import Ruble
from dollars import Dollar
from euros import Euro
r = Ruble(100)
d = Dollar(10)
e = Euro(70)
q = int(input("Введите кол-во рублей: "))
w = int(input("Введите кол-во долларов: "))
t = int(input("Введите кол-во евро: "))
r.value = q
d.value = w
e.value = t
print(f"{r.value} рублей")
print(f"{d.value} долларов")
print(f"{e.value} евро")
a = int(input('''Выберете валюту в которую будете добавлять:
1 - рубли 
2 - доллары
3 - евро
'''))
if a == 1:
    b = int(input('''выберите валюту из которой будете добавлять:
1 - доллары
2 - евро 
'''))
    if b == 1:
        r.add(d)
    elif b == 2:
        r.add(e)
    print(f"{r.value} рублей")
elif a == 2:
    b = int(input('''выберите валюту из которой будете добавлять:
1 - рубли
2 - евро 
'''))
    if b == 1:
        d.add(r)
    elif b == 2:
        d.add(e)
    print(f"{d.value} долларов")
elif a == 3:
    b = int(input('''выберите валюту из которой будете добавлять:
1 - рубли
2 - доллары
'''))
    if b == 1:
        e.add(r)
    elif b == 2:
        e.add(d)
    print(f"{e.value} евро")