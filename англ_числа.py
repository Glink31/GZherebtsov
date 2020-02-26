ones = ['','one','two','three','four','five','six','seven','eight','nine']
tens = ['','','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
teens = ['ten','eleven','twelve','thirteen','nineteen','sixteen','seventeen','eighteen','nineteen']
orders = ['','thousand','million','billion']
a = int(input('Введите число: '))
x = 0
while a > 0 and x < len(orders):
    exc = False
    emp = True
    hun = False
    b = a % 1000 
    for i in range (len(ones)):
        if i == b//100 and i == 0:
            n3 = ['']
        elif i == b//100:
            n3 = [ones[i]]
            hun = True
            emp = False
        if (b%100)//10 == 1 and i == a%10:
            n2 = [teens[i]]
            exc = True
            emp = False
        elif i == b and i > 1:
            n2 = [tens[i]]
            emp = False
        else:
            n2 = ['']
        if i == b%10 and not exc:
            n1 = [ones[i]]
            emp = False
        elif exc:
            n1 = ['']
    if not emp:
        if hun:
            print(n3[0],'hundred ',n2[0],n1[0],orders[x],end='')
        else:
            print(n3[0],n2[0],n1[0],orders[x],end='')
    a = a // 1000
    x += 1
print() 