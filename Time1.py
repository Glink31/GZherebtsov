from TimeInvalid import InvalidTimeException
class Time:
    def __init__ (self, hour, minute, second):
        self.__second = second
        self.__minute = minute
        self.__hour = hour
 
    @property
    def second(self):
        return self.__second
    @property
    def minute(self):
        return self.__minute
    @property
    def hour(self):
        return self.__hour
 
    @hour.setter
    def hour(self, new_hour):
        if new_hour >= 0 and new_hour < 24:
            self.__hour = new_hour
        elif new_hour < 0:
            raise InvalidTimeException("Час не может быть отрицательным числом")
        else:
            raise InvalidTimeException("Час не может быть больше 24")
 
    @minute.setter
    def minute(self, new_minute):
        if new_minute >= 0 and new_minute < 60:
            self.__minute = new_minute
        elif new_minute < 0:
            raise InvalidTimeException("Минута не может быть отрицательным числом")
        else:
            raise InvalidTimeException("Минута не может быть больше 59")
 
    @second.setter
    def second(self, new_second):
        if new_second >= 0 and new_second < 60:
            self.__second = new_second
        elif new_second < 0:
            raise InvalidTimeException("Секунда не может быть отрицательным числом")
        else:
            raise InvalidTimeException("Секунда не может быть больше 59")
    def next_day(self,day):
        pass
    def shiftseconds(self,shiftsec):
        leftdays = 0
        if shiftsec >= 0:
            self.__second = self.__second + shiftsec
            if self.__second//60 > 0:
                self.__minute = self.__minute + self.__second//60
                self.__second = self.__second%60
                if self.__minute//60 > 0:
                    self.__hour = self.__hour + self.__minute//60
                    self.__minute = self.__minute%60
                    if self.__hour//24 > 0:
                        leftdays = self.__hour//24
                        self.__hour = self.__hour%24
                        self.next_day(leftdays)
        else:
            leftdays = 0
            self.__second = self.__second + shiftsec
            if self.__second < 0:
                self.__minute = self.__minute + self.__second//60
                if self.__second%60 != 0:
                    self.__second =  self.__second%60
                else:
                    self.__second = 0
                if self.__minute < 0:
                    self.__hour = self.__hour + self.__minute//60
                    if self.__minute%60 != 0:
                        self.__minute = self.__minute%60
                    else: self.__minute = 0
                    if self.__hour < 0:
                        leftdays = self.__hour//24
                        self.__hour = self.__hour%24
                        self.next_day(leftdays)
    pass