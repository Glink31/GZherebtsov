from currency import Currency
class Euro(Currency):
    @property
    def value(self):
        return self.val//90
    
    @value.setter
    def value(self,val):
        self.val = val * 90
    pass