from student import Student
import random
class girl(Student):
    def __init__(self):
        self.amount = 0
    def workout(self):
        self.amount = random.randint(15,25)
        print(f"Сделала {self.amount} приседаний")
        if self.amount >= 20:
            print("Сдала")
        else:
            print("не сдала")
    pass