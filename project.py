import os
import struct
students = []

if os.path.exists("pupils.bin"):
    f = open("pupils.bin","rb")
    p = f.read(2)
    q = struct.unpack("H",p)[0]
    for i in range (q):
        students.append({})
        r = f.read(2)
        s = struct.unpack("H",r)[0]
        t = f.read(s)
        u = t.decode("utf-8")
        students[i]["last_name"] = u
        v = f.read(2)
        w = struct.unpack("H",v)[0]
        x = f.read(w)
        y = x.decode("utf-8")
        students[i]["first_name"] = y
        ad = f.read(2)
        ae = struct.unpack("H",ad)[0]
        af = f.read(ae)
        ag = af.decode("utf-8")
        students[i]["teacher"] = ag
        students[i]["marks"] = []
        ah = f.read(2)
        if ah:
            ai = struct.unpack("H",ah)[0]
            for j in range(ai):
                students[i]["marks"].append({})
                cc = f.read(2)
                cd = struct.unpack("H",cc)[0]
                aj = f.read(2)
                ak = struct.unpack("H",aj)[0]
                al = f.read(ak)
                am = al.decode("utf-8")
                students[i]["marks"][j]["date"] = am
                an = f.read(2)
                ao = struct.unpack("H",an)[0]
                ap = f.read(ao)
                aq = ap.decode("utf-8")
                students[i]["marks"][j]["presence"] = aq
                if cd > 2:
                    ar = f.read(2)
                    at = struct.unpack("H",ar)[0]
                    au = f.read(at)
                    av = au.decode("utf-8")
                    students[i]["marks"][j]["result"] = av
    f.close()

def infile():
    f = open("pupils.bin","wb")
    a = struct.pack("H",len(students))
    f.write(a)
    for i in range(len(students)):
        b = students[i]["last_name"].encode("utf-8")
        c = struct.pack("H",len(b))
        f.write(c)
        f.write(b)
        d = students[i]["first_name"].encode("utf-8")
        e = struct.pack("H",len(d))
        f.write(e)
        f.write(d)
        l = students[i]["teacher"].encode("utf-8")
        m = struct.pack("H",len(l))
        f.write(m)
        f.write(l)
        if len(students[i]["marks"]) > 0:
            g = struct.pack("H",len(students[i]["marks"]))
            f.write(g)
            for j in range (len(students[i]["marks"])):
                cb = struct.pack("H",len(students[i]["marks"][j]))
                f.write(cb)
                bc = students[i]["marks"][j]["date"].encode("utf-8")
                bd = struct.pack("H",len(bc))
                f.write(bd)
                f.write(bc)
                be = students[i]["marks"][j]["presence"].encode("utf-8")
                bf = struct.pack("H",len(be))
                f.write(bf)
                f.write(be)
                if len(students[i]["marks"][j]) > 2:
                    bg = students[i]["marks"][j]["result"].encode("utf-8")
                    bh = struct.pack("H",len(bg))
                    f.write(bh)
                    f.write(bg)
    f.close()

def descfull(i):
    print(f" === {i+1} === ")
    print("Фамилия: ",end="")
    print(students[i]["last_name"])
    print("Имя: ",end="")
    print(students[i]["first_name"])
    print("Учитель: ",end="")
    print(students[i]["teacher"])
    for j in range (len(students[i]["marks"])):
        print(f"Урок от ",end="")
        print(students[i]["marks"][j]["date"]," ",end="")
        print(students[i]["marks"][j]["presence"]," ",end="")
        if len(students[i]["marks"][j]) > 2:
            print(students[i]["marks"][j]["result"]," ",end="")
        print()

def descshort(i):
    print(f"{i+1}. ",end="")
    print(students[i]["last_name"],end="")
    print(" ",end="")
    print(students[i]["first_name"],end="")
    print(" учитель: ",end="")
    print(students[i]["teacher"])

def menu1():
    print("1. Список учеников")
    print("2. Отметить класс")
    print("3. Добавить ученика")
    print("4. Изменить ученика")
    print("5. Удалить ученика")
    print("6. Поиск")
    print("7. Выход")

def menu2():
    print("1. Изменить фамилию")
    print("2. Изменить имя")
    print("3. Изменить учителя")
    print("4. Добавить оценку")
    print("5. Изменить оценку")
    print("6. Удалить оценку")
    print("7. Назад")

def menu3():
    print("1. Поиск по учителю")
    print("2. Поиск по уроку")
    print("3. Показать неуспевающих")
    print("4. Показать успевающих")
    print("5. Назад")

def markred():
    print("1. Изменить дату")
    print("2. Изменить присутствие")
    print("3. Изменить результат")
    print("4. Назад")

menu1()
an = int(input("Выберите действие: "))
while an:
    if an == 1:
        if len(students) == 0:
            print("учеников нет")
        else:
            for i in range (len(students)):
                descfull(i)
    elif an == 2:
        if len(students) > 0:
            bx = str(input("Введите имя учителя: "))
            found = True
            ca = 0
            for i in range(len(students)):
                if bx in students[i]["teacher"]:
                    if ca == 0:
                        by = str(input("Введите дату урока ДД/ММ/ГГ: "))
                        ca +=1
                    found = False
                    descshort(i)
                    bz = str(input("Этот ученик был на онлайн уроке? был/не был: "))
                    lesson = {}
                    lesson["date"] = by
                    lesson["presence"] = bz
                    students[i]["marks"].append(lesson)
                    infile()
            if found:
                print("Такого учителя нет")
        else:
            print("Учеников нет")

    elif an == 3:
        ao = str(input("Введите фамилию ученика: "))
        ap = str(input("Введите имя ученика: "))
        aq = str(input("Введите учителя: "))
        pupil = {}
        pupil["last_name"] = ao
        pupil["first_name"] = ap
        pupil["teacher"] = aq
        pupil["marks"] = []
        students.append(pupil)
        infile()
    elif an == 4:
        if len(students) == 0:
            print("Студентов нет")
        else:
            for i in range (len(students)):
                descshort(i)
            ar = int(input("Выберите ученика: "))
            if ar > 0 and ar <= len(students):
                menu2()
                at = int(input("Выберите действие: "))
                while at == 0:
                    print("Ввод неверен")
                    at = int(input("Выберите действие: "))
                while at > 0:
                    if at == 1:
                        au = str(input("Введите новую фамилию: "))
                        students[ar-1]["last_name"] = au
                        infile()
                    elif at == 2:
                        av = str(input("Введите новое имя: "))
                        students[ar-1]["first_name"] = av
                        infile()
                    elif at == 3:
                        aw = str(input("Введите нового учителя: "))
                        students[ar-1]["teacher"] = aw
                        infile()
                    elif at == 4:
                        bh = str(input(f"Введите дату проведения урока  ДД/ММ/ГГ: "))
                        bk = str(input(f"Присутствовал ли ученик на онлайн уроке? был/не был: "))
                        bl = str(input(f"Введите оценку ученика за урок Зачёт/Незачёт: "))
                        students[ar-1]["marks"].append({})
                        students[ar-1]["marks"][len(students[ar-1]["marks"])-1]["date"] = bh
                        students[ar-1]["marks"][len(students[ar-1]["marks"])-1]["presence"] = bk
                        students[ar-1]["marks"][len(students[ar-1]["marks"])-1]["result"] = bl
                        infile()                                   
                    elif at == 5:
                        if len(students[ar-1]["marks"]) > 0:
                            descfull(ar-1)
                            Found = False
                            bm = str(input("Введите дату урока который нужно изменить ДД/ММ/ГГ: "))
                            for j in range(len(students[i]["marks"])):
                                if bm in students[i]["marks"][j]["date"]:
                                    Found = True
                                    markred()
                                    bn = int(input("Выберите действие: "))
                                    while bn >= 0:
                                        if bn == 1:
                                            bo = str(input("Введите новую дату ДД/ММ/ГГ: "))
                                            students[ar-1]["marks"][j]["date"] = bo
                                            infile()
                                        elif bn == 2:
                                            bp = str(input("Введите новые данные по присутствию был/не был: "))
                                            students[ar-1]["marks"][j]["presence"] = bp
                                            infile()
                                        elif bn == 3:
                                            bq = str(input("Введите новую оценку Зачёт/Незачёт: "))
                                            students[ar-1]["marks"][j]["result"] = bq
                                            infile()
                                        elif bn == 4:
                                            break
                                        else:
                                            print("Ввод неверен")
                                        markred()
                                        bn = int(input("Выберите действие: "))
                            if not Found:
                                print("Такого урока нет")
                        else:
                            print("У ученика нет уроков")
                    elif at == 6:
                        if len(students[ar-1]["marks"]) > 0:
                            descfull(ar-1)
                            Found = False
                            bo = str(input("Введите дату урока который нужно удалить: "))
                            for j in range(len(students[i]["marks"])):
                                if bo in students[i]["marks"][j]["date"]:
                                    Found = True
                                    inp = False
                                    while not inp:
                                        bp = str(input(f"Вы уверены что хотите удалить урок {bo}? Да/Нет: "))
                                        if bp == "Да":
                                            del(students[ar-1]["marks"][j])
                                            inp = True
                                            infile()
                                        elif bp == "Нет":
                                            inp = True
                                        else:
                                            print("Ввод неверен")
                            if not Found:
                                print("Такого урока нет")
                        else:
                            print("У ученика нет уроков")
                    elif at == 7:
                        break
                    else:
                        print("Ввод неверен")
                    menu2()
                    at = int(input("Выберите действие: "))
                        
    elif an == 5:
        for i in range(len(students)):
            descshort(i)
        br = int(input("Введите номер ученика которого нужно удалить: "))
        if br > 0 and br <= len(students):
            inp = False
            while not inp:
                bs = str(input(f"Вы уверены, что хотите удалить ученика {br}? Да/Нет: "))
                if bs == "Да":
                    del(students[br-1])
                    inp = True
                    infile()
                elif bs == "Нет":
                    inp = True
                else:
                    print("Ввод неверен")
            else:
                print("Ввод неверен")
    elif an == 6:
        menu3()
        bt = int(input("Выберите действие: "))
        while bt == 0:
            print("Ввод неверен")
            menu3()
            bt = int(input("Выберите действие: "))
        while bt > 0:
            if bt == 1:
                bu = str(input("Введите учителя: "))
                Found = False
                for i in range(len(students)):
                    if bu in students[i]["teacher"]:
                        Found = True
                        bw = 0
                        if len(students[i]["marks"]) > 0:
                            good = True
                            for j in range(len(students[i]["marks"])):
                                if students[i]["marks"][j]["result"] == "Незачёт":
                                    good = False
                            if good:
                                bw += 1
                        print(f"У этого учителя {bw} успевающих учеников")
                        descfull(i)
                if not Found:
                    print("Такого учителя нет")
            elif bt == 2:
                bv = str(input("Введите дату урока ДД/ММ/ГГ: "))
                Found = False
                for i in range(len(students)):
                    for j in range (len(students[i]["marks"])):
                        if bv in students[i]["marks"][j]["date"]:
                            Found = True
                            descshort(i)
                            print(f"Урок ",end="")
                            print(students[i]["marks"][j]["date"]," ",end="")
                            print(students[i]["marks"][j]["presence"]," ",end="")
                            print(students[i]["marks"][j]["result"])
                if not Found:
                    print("Урока за эту дату нет")
            elif bt == 3:
                if len(students) > 0:
                    for i in range(len(students)):
                        pri = False
                        for j in range(len(students[i]["marks"])):
                            if students[i]["marks"][j]["result"] == "Незачёт" :                       
                                if not pri:
                                    descshort(i)
                                    pri = True
                                print(students[i]["marks"][j]["date"]," ",end="")
                                print(students[i]["marks"][j]["presence"]," ",end="")
                                print(students[i]["marks"][j]["result"])
            elif bt == 4:
                if len(students) > 0:
                    for i in range(len(students)):
                        if len(students[i]["marks"]) > 0:
                            good = True
                            for j in range(len(students[i]["marks"])):
                                if students[i]["marks"][j]["result"] == "Незачёт":
                                    good = False
                            if good:
                                descshort(i)
            elif bt == 5:
                break
            else:
                print("Ввод неверен")
            menu3()
            bt = int(input("Выберите действие: "))
    elif an == 7:
        break
    else:
        print("Ввод неверен")
    menu1()
    an = int(input("Выберите действие: "))
