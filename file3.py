f = open("filetask1.txt", "r")
s = f.readline()
while s != "":
    v = int(s)
    print(v*2)
    s = f.readline()