import struct 
n = int(input("Введите положительное число: "))
f = open("bytetask1.bin","wb")
for i in range (1,n+1):
    buffer = struct.pack("H",i)
    f.write(buffer)
f.close()