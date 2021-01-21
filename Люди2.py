import struct 
f = open("humans.bin","rb")
s =  f.read(2)
c = struct.unpack("H",s)[0]
people = []
for i in range(c):
    z = f.read(2)
    v = struct.unpack("H",z)[0]
    person = {}
    x = f.read(2)
    b = struct.unpack("H",x)[0]
    n = f.read(b)
    m = n.decode("utf-8")
    person['last_name'] = m
    d = f.read(2)
    g = struct.unpack("H",x)[0]
    h = f.read(g)
    k = n.decode("utf-8")
    person['first_name'] = k
    a = f.read(2)
    s = struct.unpack("H",a)[0]
    person['age'] = s
    people.append(person)
for i in range (len(people)):
    for j in people[i].values:
        print(j)