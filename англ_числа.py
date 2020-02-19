ones = ['','one','two','three','four','five','six','seven','eight','nine']
tens = ['','','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
teens = ['ten','eleven','twelve','thirteen','nineteen','sixteen','seventeen','eighteen','nineteen']
orders = ['','thousand','million','billion']
a = int(input('Введите число: '))
x = 1
while a > 0:    
    b = a // (len(orders)*3-2)
    for i in range (len(ones)):
        if i == b//100 and i != 0:
            print(ones[i],'hundred ',end="")
        elif i == b//100:
            print (ones[i]," ",end="")
        if i == b%10 and (b%100)//10 == 1:
            print(teens[i]," ",end="")
        elif i == (b%100)//10:
            print(tens[i]," ",end="")
        if i == b%10:
            print (ones[i]," ",end="")
    print(orders[x-1],end="")
    a = a % (len(orders)*3-2*x)
    x += 1
print()