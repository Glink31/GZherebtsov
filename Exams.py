import os
import struct
sts = []
def printing():
    for i in range (len(sts)):
        print(f"{i+1}. ",end="")
        print(sts[i]["last_name"],end="")
        print(" ",end="")
        print(sts[i]["first_name"],end="")
        print(" ",end="")
        print(sts[i]["patronymic"],end="")
        print(" ",end="")
        print(sts[i]["group"])
        
def desc(i):
    print(f" === {i+1} === ")
    print("Фамилия: ",end="")
    print(sts[i]["last_name"])
    print("Имя: ",end="")
    print(sts[i]["first_name"])
    print("Отчество: ",end="")
    print(sts[i]["patronymic"])
    print("Группа: ",end="")
    print(sts[i]["group"])
    if len(sts[i]["marks"]) == 0:
        print("Оценок нет")
    else:
        print("оценки: ")
        for j,k in sts[i]["marks"].items():
            print(f"  {j}: {k}")

def infile():
    f = open("students.bin","wb")
    g = struct.pack("H",len(sts))
    f.write(g)
    for i in range(len(sts)):
        h = sts[i]["last_name"].encode("utf-8")
        l = struct.pack("H",len(h))
        f.write(l)
        f.write(h)
        m = sts[i]["first_name"].encode("utf-8")
        n = struct.pack("H",len(m))
        f.write(n)
        f.write(m)
        o = sts[i]["patronymic"].encode("utf-8")
        p = struct.pack("H",len(o))
        f.write(p)
        f.write(o)
        q = sts[i]["group"].encode("utf-8")
        r = struct.pack("H",len(q))
        f.write(r)
        f.write(q)
        if len(sts[i]["marks"]) > 0:
            ab = struct.pack("H",len(sts[i]["marks"]))
            f.write(ab)
            for j,k in sts[i]["marks"].items():
                ac = j.encode("utf-8")
                ad = struct.pack("H",len(ac))
                f.write(ad)
                f.write(ac)
                ae = struct.pack("H",k)
                f.write(ae)
    f.close()

if os.path.exists("students.bin"):
    f = open("students.bin","rb")
    s = f.read(2)
    t = struct.unpack("H",s)[0]
    for i in range(t):
        sts.append({})
        u = f.read(2)
        al = struct.unpack("H",u)[0]
        am = f.read(al)
        an = am.decode("utf-8")
        sts[i]["last_name"] = an 
        ao = f.read(2)
        ap = struct.unpack("H",ao)[0]
        aq = f.read(ap)
        ar = aq.decode("utf-8")
        sts[i]["first_name"] = ar
        at = f.read(2)
        au = struct.unpack("H",at)[0]
        av = f.read(au)
        aw = av.decode("utf-8")
        sts[i]["patronymic"] = aw
        ax = f.read(2)
        ay = struct.unpack("H",ax)[0]
        az = f.read(ay)
        ba = az.decode("utf-8")
        sts[i]["group"] = ba
        bb = f.read(2)
        if bb:
            sts[i]["marks"]={}
            bc = struct.unpack("H",bb)[0]
            for j in range(bc):
                bd = f.read(2)
                be = struct.unpack("H",bd)[0]
                bf = f.read(be)
                bg = bf.decode("utf-8")
                bh = f.read(2)
                bi = struct.unpack("H",bh)[0]
                sts[i]["marks"][bg] = bi
        else:
            sts[i]["marks"] = {}
    f.close()

print("1. Список студентов")
print("2. Добавить студента")
print("3. Редактировать студента")
print("4. Удалить студента")
print("5. Показать отличников")
print("6. Показать неуспевающих")
print("7. Выход")
a = int(input("Выберите действие: "))
while a > 0:
    if a == 1:
        if len(sts) == 0:
            print("студентов нет")
        else:
            for i in range(len(sts)):
                desc(i)
    elif a == 2:
        b = str(input("Введите фамилию студента: "))
        c = str(input("Введите имя студента: "))
        d = str(input("Введите отчество студента: "))
        e = str(input("Введите группу студента: "))
        student = {}
        student["last_name"] = b
        student["first_name"] = c
        student["patronymic"] = d
        student["group"] = e
        student["marks"] = {}
        sts.append(student)
        infile()
    elif a == 3:
        if len(sts) == 0:
            print("Студентов нет")
        else:
            printing()
            v = int(input("Выберете студента: "))
            if v <= len(sts) and v > 0:    
                print("1. Изменить фамилию")
                print("2. Изменить имя")
                print("3. Изменить отчество")
                print("4. Изменить группу")
                print("5. Добавить оценку")
                print("6. Изменить оценку")
                print("7. Удалить оценку")
                print("8. Назад")
                w = int(input("Выберете действие: "))
                while w > 0:
                    if w == 1:
                        x = str(input("Введите новую фамилию: "))
                        sts[v-1]["last_name"] = x
                        infile()
                    elif w == 2:
                        y = str(input("Введите новое имя: "))
                        sts[v-1]["first_name"] = y
                        infile()
                    elif w == 3:
                        z = str(input("Введите новое отчество: "))
                        sts[v-1]["patronymic"] = z
                        infile()
                    elif w == 4:
                        aa = str(input("Введите новую группу: " ))
                        sts[v-1]["group"] = aa
                        infile()
                    elif w == 5:
                        af = str(input("Введите предмет: "))
                        exist = False
                        if len(sts[i]["marks"]) > 0:
                            if af in sts[i]["marks"]:
                                    exist = True
                            if not exist:
                                ag = int(input("Введите оценку студента: "))
                                sts[v-1]["marks"][af] = ag
                                infile()
                            else:
                                print("У данного студента уже есть оценка по этому предмету!")
                        else:
                            ag = int(input("Введите оценку студента: "))
                            sts[v-1]["marks"][af] = ag
                            infile()
                    elif w == 6:
                        if len(sts[i]["marks"]) > 0:
                            ah = str(input("Введите предмет по которому нужно изменить оценку: "))
                            exist = False
                            if ah in sts[i]["marks"]:
                                    exist = True
                            if exist:
                                ai = int(input("Введите оценку: "))
                                sts[v-1]["marks"][ah] = ai
                                infile()
                            else:
                                print("Такого предмета у данного студента нет")
                        else:
                            print("У студента нет оценок")
                    elif w == 7:
                        if len(sts[v-1]["marks"]) > 0:
                            aj = str(input("Введите предмет который нужно удалить: "))
                            exist = False
                            if aj in sts[v-1]["marks"]:
                                    exist = True
                            if exist:
                                ak = str(input("Вы уверены что хотите удалить оценку? Y/N: "))
                                inp = False
                                while not inp:
                                    if ak == "Y":
                                        del(sts[v-1]["marks"][aj])
                                        inp = True
                                        infile()
                                    elif ak == "N":
                                        inp = True
                                    else:
                                        print("Ввод неверен")
                            else:
                                print("Такого предмета у данного студента нет")
                        else:
                            print("У студента нет оценок")
                    elif w == 8:
                        break
                    else:
                        print("Ввод неверен")
                    print("1. Изменить фамилию")
                    print("2. Изменить имя")
                    print("3. Изменить отчество")
                    print("4. Изменить группу")
                    print("5. Добавить оценку")
                    print("6. Изменить оценку")
                    print("7. Удалить оценку")
                    print("8. Назад")
                    w = int(input("Выберете действие: "))
            else:
                print("Такого студента нет")
    elif a == 4:
        if len(sts) > 0:
            printing()
            bj = int(input("Выберите студента которого хотите удалить: "))
            if bj > 0 and bj <= len(sts):
                bk = str(input(f"Вы уверены что хотите удалить студента {bj}? Y/N "))
                inp = False
                while not inp:
                    if bk == "Y":
                        del(sts[bj-1])
                        inp = True
                        infile()
                    elif bk == "N":
                        inp = True
                    else:
                        print("Ввод неверен")
            else:
                print("Такого студента нет")
        else:
            print("Студентов нет")
    elif a == 5:
        if len(sts) > 0:
            for i in range(len(sts)):
                if len(sts[i]["marks"]) > 0:
                    good = True
                    for j in sts[i]["marks"].values():
                        if j < 5:
                            good = False
                    if good:
                        desc(i)
        else:
            print("Студентов нет")
    elif a == 6:
        if len(sts) > 0:
            for i in range(len(sts)):
                for j in sts[i]["marks"].values():
                    if j == 2:
                        desc(i)
                        break
        else:
            print("Студентов нет")
    elif a == 7:
        break
    else:
        print("Ввод неверен")
    print("1. Список студентов")
    print("2. Добавить студента")
    print("3. Редактировать студента")
    print("4. Удалить студента")
    print("5. Показать отличников")
    print("6. Показать неуспевающих")
    print("7. Выход")
    a = int(input("Выберите действие: "))