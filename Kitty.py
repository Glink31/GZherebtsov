class Cat:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def noise(self):
        print("meow")
    
    def feed(self):
        print(f"{self.name} накормлен")

a = "уголёк"
b = "чёрный"
c = "рыжик"
d = "рыжий"
c1 = Cat(a,b)
c2 = Cat(c,d)
c1.noise()
c1.feed()
c2.noise()
c2.feed()