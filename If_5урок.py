x1 = int(input("Введите координату x для левого верхнего угла "))
y1 = int(input("Введите координату y для левого верхнего угла "))
w = int(input("Введите длину прямоугольника "))
h = int(input("Введите ширину прямоугольника "))
x2 = int(input("Введите координату x "))
y2 = int(input("Введите координату y "))
if ((x2 < x1) or (x2 > (x1+w))) or ((y2 > y1) or (y2 < (y1-h))):
    print (f"точка находится за прямоугольником")
elif ((x2 > x1) and (x2 < (x1 + w))) and ((y2 < y1) and (y2 > (y1 - h))):
    print (f"точка находится внутри прямоугольника")
else:
    print (f"точка находится на грани прямоугольника")
