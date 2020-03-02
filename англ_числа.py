ones = ['','one','two','three','four','five','six','seven','eight','nine']
tens = ['','','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
teens = ['ten','eleven','twelve','thirteen','nineteen','sixteen','seventeen','eighteen','nineteen']
orders = ['','thousand','million','billion']
a = int(input('Введите число: '))
x = 0
k = ''
while a != 0 and x < len(orders):
    exc = False
    emp = False
    hun = False
    b = a % 1000 
    if b//100 == 0:
        n3 = ''
    elif b//100 > 0:
        n3 = ones[b//100]
        hun = True
    if (b//10)%10 == 1:
        n2 = teens[b%10]
        exc = True 
    elif (b//10)%10 > 1:
        n2 = tens[(b//10)%10]
    else:
        n2 = ''
    if not exc:
        n1 = ones[b%10]
    else:
        n1 = ''
    if b%10 == 0 and (b//10)%10 == 0 and b//100 == 0:
        emp = True
    if not emp:
        if hun:
            f=n3+' '+'hundred '+n2+' '+n1+' '+orders[x]+' '
            k = f + k
        else:
            f=n3+' '+n2+' '+n1+' '+orders[x]+' '
            k = f + k
    a = a // 1000
    x += 1
print(k)