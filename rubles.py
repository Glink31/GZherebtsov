from currency import Currency
class Ruble(Currency):
    @property
    def value(self):
        return self.val

    @value.setter
    def value(self,val):
        self.val = val
    pass