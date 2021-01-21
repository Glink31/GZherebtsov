from cat import Cat
from dog import Dog
from cow import Cow
def sayThing(p):
    p.say()
a = Cat()
b = Dog()
c = Cow()
sayThing(a)
sayThing(b)
sayThing(c)