n = int(input("Введите число: "))
k = open("filetask2.txt","w")
for i in range (1,n+1):
    k.write(f"{i} ")
k.close