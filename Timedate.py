from Time1 import Time
from DateInvalid import InvalidDateException
class DateTime(Time):
    def __init__(self,hour,minute,second,day,month,year):
        super().__init__(hour, minute, second)
        self.__day = day
        self.__month = month
        self.__year = year
    @staticmethod
    def is_leap(year):
        return (year%4 == 0 and year % 100 != 0) or year%400 == 0
    @staticmethod
    def days_in_month(month, year):
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 or month == 0:
            return 31
        elif month == 4 or month == 6 or month == 9 or month == 11:
            return 30
        elif month == 2:
            if DateTime.is_leap(year):
                return 29
            else:
                return 28
    @property
    def year(self):
        return self.__year
    @property
    def month(self):
        return self.__month
    @property
    def day(self):
        return self.__day
    @year.setter
    def year(self,new_year):
        if new_year != 0:
            self.__year = new_year
        else:
            raise InvalidDateException("Номер года не может быть равен 0") 
    @month.setter
    def month(self,new_month):
        if new_month <= 12 and new_month > 0:
            self.__month = new_month
        elif new_month == 0:
            raise InvalidDateException("Номер месяца не может быть равен 0")
        elif new_month < 0:
            raise InvalidDateException("Номер месяца не может быть меньше 0")
        else:
            raise InvalidDateException("Номер года не может быть больше 12")
    @day.setter
    def day(self,new_day):
        if new_day > 0 and new_day <= self.days_in_month(self.__month,self.__year):
            self.__day = new_day
        elif new_day == 0:
            raise InvalidDateException("Номер дня не может быть равен 0")
        elif new_day < 0:
            raise InvalidDateException("Номер дня не может быть меньше 0")
        else:
            raise InvalidDateException(f"Номер дня для месяця {self.__month} не может быть больше {self.days_in_month(self.__month,self.__year)}")
    def next_day(self,day):
            self.shiftday(day)
    def shiftday(self,shift):
        if shift >= 0:
            self.__day += shift
            while self.__day > DateTime.days_in_month(self.__month,self.__year):
                h = DateTime.days_in_month(self.__month,self.__year)
                self.__month += 1
                self.__day -= h
                if self.__month > 12:
                    self.__year += 1
                    self.__month -= 12
        else:
            self.__day += shift
            while self.__day < 1:
                self.__month -= 1
                h = DateTime.days_in_month(self.__month,self.__year)
                self.__day = self.__day + h
                if self.__month < 1:
                    self.__year -= 1
                    self.__month = 12 + self.__month
                if self.__year == 0:
                    self.__year = -1
        
y = DateTime(0,0,0,1,1,1)
try:
    d = int(input("Введите год: "))
    y.year = d
except ValueError as d:
    print(f"неверная переменная")
try:
    e = int(input("Введите месяц: "))
    y.month = e
except ValueError as e:
    print(f"неверная переменная")
try:
    f = int(input("Введите день: "))
    y.day = f
except ValueError as f:
    print(f"неверная переменная")
try:
    a = int(input("Введите часы: "))
    y.hour = a
except ValueError as a:
    print(f"неверная переменная")
try:
    b = int(input("Введите минуты: "))
    y.minute = b
except ValueError as b:
    print(f"неверная переменная")
try:
    c = int(input("Введите секунды: "))
    y.second = c
except ValueError as c:
    print(f"неверная переменная")
print(f"Дата: {y.day}.{y.month}.{y.year} Время: {y.hour}:{y.minute}:{y.second}")
try:
    s = int(input("Введите на сколько сдвинуть секунды: "))
    y.shiftseconds(s)
except ValueError as s:
    print(f"неверная переменная")
print(f"Дата: {y.day}.{y.month}.{y.year} Время: {y.hour}:{y.minute}:{y.second}")
try:
    l = int(input("Введите на сколько сдвинуть дни: "))
    y.shiftday(l)
except ValueError as l:
    print(f"неверная переменная")
print(f"Дата: {y.day}.{y.month}.{y.year} Время: {y.hour}:{y.minute}:{y.second}")