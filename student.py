from abc import ABCMeta, abstractmethod
class Student(metaclass=ABCMeta):
    @abstractmethod
    def workout(self):
        pass
    