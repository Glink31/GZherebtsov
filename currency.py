from abc import ABCMeta, abstractmethod
class Currency(metaclass=ABCMeta):
    def __init__(self,val):
        self.val = val
        pass  
    def add(self,cur):
        self.val += cur.val
        pass
    @property
    @abstractmethod
    def value(self):
        pass
    @value.setter
    @abstractmethod
    def value(self,val):
        pass
        
    