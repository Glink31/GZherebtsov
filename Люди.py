import struct 
people = []
a = str(input("Введите фамилию: "))
while a != "exit":
    b = str(input("Введите имя: "))
    c = int(input("Введите возраст: "))
    person = {}
    person['last_name'] = a
    person['first_name'] = b
    person['age'] = c
    people.append(person)
    a = str(input("Введите фамилию: "))
f = open("humans.bin","wb")
p = struct.pack("H",len(people))
f.write(p)
for i in range(len(people)):
    g = struct.pack("H",3)
    f.write(g)
    t = people[i]["last_name"]
    b = t.encode("utf-8")
    v = struct.pack("H",len(b))
    f.write(v)
    f.write(b)
    e = people[i]["first_name"]
    d = e.encode("utf-8")
    m = struct.pack("H",len(d))
    f.write(m)
    f.write(d)
    z = struct.pack("H",people[i]["age"])
    f.write(z)
f.close()
