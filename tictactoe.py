import os
def checkwin (x:str):
    if (field[0][0] == x and field[0][1] == x and field[0][2] == x) or (field[1][0] == x and field[1][1] == x and field[1][2] == x) or (field[2][0] == x and field[2][1] == x and field[2][2] == x) or (field[0][0] == x and field[1][0] == x and field[2][0] == x) or (field[0][1] == x and field[1][1] == x and field[2][1] == x) or (field[0][2] == x and field[1][2] == x and field[2][2] == x) or (field[0][0] == x and field[1][1] == x and field[2][2] == x) or (field[0][2] == x and field[1][1] == x and field[2][0] == x):
        win1 = True
    else:
        win1 = False
    return win1
score = {}
winn = []
if os.path.exists("winners.txt"):
    f = open("winners.txt", "r")
    s = f.readline()
    while s:
        winn = s.split()
        score[winn[0]] = int(winn[1])
        s = f.readline()
    f.close()
y = str(input("Введите имя игрока X: "))
z = str(input("Введите имя игрока O: "))
yp = False
zp = False
for key in score.keys():
    if y == key:
        yp = True
    if z == key:
        zp = True
if not yp:
    score[y] = 0
if not zp:
    score[z] = 0
play = True
while play:
    emp=['A1','A2','A3','B1','B2','B3','C1','C2','C3']
    field=[[" "," "," "],[" "," "," "],[" "," "," "]]
    j=0
    win = False
    for i in range (3):
        print("+-+-+-+")
        print(f"|{field[i][0]}|{field[i][1]}|{field[i][2]}|")
    print("+-+-+-+")
    while j != 9:
        win = checkwin("O")
        if win:
            print("O победил")
            score[z] += 1
            break
        inp = False
        while not inp:
            a=str(input("ход X: "))
            if a[0] == emp[0][0] or a[0] == emp[1][0] or a[0] == emp[2][0]:
                if a[1] == emp[0][1]:
                    field[0][0] = "X"
                    emp[0] = '  '
                    j+=1
                    inp = True
                elif a[1] == emp[1][1]:
                    field[0][1] = "X"
                    emp[1] = '  '
                    j+=1
                    inp = True
                elif a[1] == emp[2][1]:
                    field[0][2] = "X"
                    emp[2] = '  '
                    j+=1
                    inp = True
                else:
                    print("Ввод неверный")
            elif a[0] == emp[3][0] or a[0] == emp[4][0] or a[0] == emp[5][0]:
                if a[1] == emp[3][1]:
                    field[1][0] = "X"
                    emp[3] = '  '
                    j+=1
                    inp = True
                elif a[1] == emp[4][1]:
                    field[1][1] = "X"
                    emp[4] = '  '
                    j+=1
                    inp = True
                elif a[1] == emp[5][1]:
                    field[1][2] = "X"
                    emp[5] = '  '
                    j+=1
                    inp = True
                else:
                    print("Ввод неверный")
            elif a[0] == emp[6][0] or a[0] == emp[7][0] or a[0] == emp[8][0]:
                if a[1] == emp[6][1]:
                    field[2][0] = "X"
                    emp[6] = '  '
                    j+=1
                    inp = True
                elif a[1] == emp[7][1]:
                    field[2][1] = "X"
                    emp[7] = '  '
                    j+=1
                    inp = True
                elif a[1] == emp[8][1]:
                    field[2][2] = "X"
                    emp[8] = '  '
                    j+=1
                    inp = True
                else:
                    print("Ввод неверный")
            else:
                print("Ввод неверный")
            for i in range (3):
                print("+-+-+-+")
                print(f"|{field[i][0]}|{field[i][1]}|{field[i][2]}|")
            print("+-+-+-+")
        win = checkwin("X")
        if win:
            print("X победил")
            score[y] += 1
            break
        inp = False
        if j == 9:
            break
        while not inp:
            a=str(input("ход O: "))
            if a[0] == emp[0][0] or a[0] == emp[1][0] or a[0] == emp[2][0]:
                if a[1] == emp[0][1]:
                    field[0][0] = "O"
                    emp[0] = '  '
                    j+=1
                    inp = True
                elif a[1] == emp[1][1]:
                    field[0][1] = "O"
                    emp[1] = '  '
                    j+=1
                    inp = True
                elif a[1] == emp[2][1]:
                    field[0][2] = "O"
                    emp[2] = '  '
                    j+=1
                    inp = True
                else:
                    print("Ввод неверный")
            elif a[0] == emp[3][0] or a[0] == emp[4][0] or a[0] == emp[5][0]:
                if a[1] == emp[3][1]:
                    field[1][0] = "O"
                    emp[3] = '  '
                    j+=1
                    inp = True
                elif a[1] == emp[4][1]:
                    field[1][1] = "O"
                    emp[4] = '  '
                    j+=1
                    inp = True
                elif a[1] == emp[5][1]:
                    field[1][2] = "O"
                    emp[5] = '  '
                    j+=1
                    inp = True
                else:
                    print("Ввод неверный")
            elif a[0] == emp[6][0] or a[0] == emp[7][0] or a[0] == emp[8][0]:
                if a[1] == emp[6][1]:
                    field[2][0] = "O"
                    emp[6] = '  '
                    j+=1
                    inp = True
                elif a[1] == emp[7][1]:
                    field[2][1] = "O"
                    emp[7] = '  '
                    j+=1
                    inp = True
                elif a[1] == emp[8][1]:
                    field[2][2] = "O"
                    emp[8] = '  '
                    j+=1
                    inp = True
                else:
                    print("Ввод неверный")
            else:
                print("Ввод неверный")
            for i in range (3):
                print("+-+-+-+")
                print(f"|{field[i][0]}|{field[i][1]}|{field[i][2]}|")
            print("+-+-+-+")
    if not win:
        print("Ничья!")
    answer = False
    while not answer:
        b = str(input("Сыграем ещё раз? Y/N "))
        if b == "N":
            play = False
            answer = True
            f = open("winners.txt", "w")
            for k,l in score.items():
                if l > 0:
                    f.write(k + " ")
                    f.write(str(l) + "\n")
                    print(f"{k} {l}")
            f.close()
        elif b == "Y":
            answer = True
        else:
            print('Неправильный ввод')