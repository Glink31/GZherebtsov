import struct 
f = open("bytetask1.bin","rb")
s = f.read(2)
while s:
    x = struct.unpack("H",s)[0]
    print(x*3)
    s = f.read(2)
f.close()