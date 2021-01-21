from student import Student
import random
class boy(Student):
    def __init__(self):
        self.amount = 0
    def workout(self):
        self.amount = random.randint(10,25)
        print(f"Сделал {self.amount} отжиманий")
        if self.amount >= 20:
            print("Сдал")
        else:
            print("не сдал")
    pass