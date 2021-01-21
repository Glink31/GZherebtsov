n = int(input("Введите число: "))
k = open("filetask1.txt","w")
for i in range (1,n+1):
    k.write(str(i)+ "\n")
k.close