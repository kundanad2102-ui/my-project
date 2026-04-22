#Polymorphism---> This allows a object of different classes to be treated as instance of the same base class,
#with methods behaving differently based on the actual object type. eg... len,
'''
print(len("Python"))
print(len([1,2,3]))
'''

#Method Overloading---> This defines multiple methods with the same name but different parameters(number,type, or order)
'''
class calculator:
    def add(self, a, b=5, c=3):
        return a+b+c
Cal= calculator()
print(Cal.add(2))
print(Cal.add(3,4))
print(Cal.add(5,7,8))
'''

'''
class calculator:
    def add(self, a, b=5, c=3):
        return a-b+c
Cal= calculator()
print(Cal.add(1))
print(Cal.add(2,3))
print(Cal.add(4,5,6))
'''

#Method Overriding--->This occurs in the child class, redefining a parent class method with the same signature for runtime
'''
class animal:
    def speak(self):
        return "Sound"
class dog(animal):
    def speak(self):
        return"Bow Bow"
DOG = dog()
print(DOG.speak())


class animal:
    def speak(self):
        return "Sound"
class cat(animal):
    def speak(self):
        return"Meow"
CAT = cat()
print(CAT.speak())
'''

#Operator Overloading---> This customises operator like +,- for user-defined classes by implementing special methods.eg: __add__, __sub__
'''
class someone:
    def  __init__(self, a, b,c):
        self.a = a
        self.b = b
        self.c = c
    def __add__(self, other):
        return someone(self.a + other.a, self.b + other.b, self.c + other.c)
    def __str__(self):
        return f"({self.a}, {self.b}), {self.c})"
any = someone(4,3,7)
so = someone(5,8,11)
print(any + so)
'''

'''
class someone:
    def  __init__(self, a, b,c):
        self.a = a
        self.b = b
        self.c = c
    def __sub__(self, other):
        return someone(self.a - other.a, self.b - other.b, self.c - other.c)
    def __str__(self):
        return f"({self.a}, {self.b}), {self.c})"
any = someone(6,3,4)
so = someone(5,2,9)
print(any - so)    
'''

#Data Abstraction---> This hides complex implementation details, exposing only essential features via abstract class or interface
'''
from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area (self):
        return 3.14 * self.radius **2
Circle = circle(5)
print(Circle.area())
'''
























    







