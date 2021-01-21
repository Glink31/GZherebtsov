from random import randint
class array:
    def __init__ (self,length):
        self.__len = length
        self.arr = []
        for i in range(length):
            a = randint(-10,10)
            self.arr.append(a)

    @property
    def length(self):
        return len(self.arr)
    
    def add_element(self,elm1):
        self.arr.append(elm1)
        self.__len = len(self.arr)
    
    def remove_element(self,elm2):
        if elm2 not in self.arr:
            print("Такого числа в массиве нет")
        else:
            self.arr.remove(elm2)
            self.__len = len(self.arr)
    
    def __str__(self):
        return f"{self.arr}"

    def __repr__(self):
        return f"<array {self.arr}>"

    def __getitem__(self,ind1):
        return self.arr[ind1]
    
    def __setitem__(self,ind2,val):
        self.arr[ind2] = val

m=int(input("Введите размер массива: "))
b = array(m)
print(f"размер массива равен {b.length}")
p = str(b)
print(p)
d = int(input("введите элемент который нужно добавить: "))
b.add_element(d)
print(f"размер массива равен {b.length}")
print(b)
e = int(input("Введите элемент для удаления: "))
b.remove_element(e)
print(f"размер массива равен {b.length}")
print(b)
h = int(input("Введите номер элемента: "))
print(b[h])
l = int(input("Введите номер элемента который хотите заменить: "))
n = int(input(f"Введите число на которое хотите заменить элемент {b[l]}: "))
b[l] = n
print(f"размер массива равен {b.length}")
print(b)