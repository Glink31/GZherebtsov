from currency import Currency
class Dollar(Currency):
    @property
    def value(self):
        return self.val//60

    @value.setter
    def value(self,val):
        self.val = val*60  
    pass