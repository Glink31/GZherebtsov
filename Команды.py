Teams = {}
a = str(input("Введите название команды: "))
while a != "exit":
    b = int(input(f"Введите кол-во очков команды {a}: "))
    Teams[a] = b
    a = str(input("Введите название команды: "))
for c,d in Teams.items():
    print(f"{c} {d}")