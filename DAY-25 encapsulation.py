#Encapsulation----> The principle of binding data(Attributes) and methods that operate on that data into a 
#simple unit, which is a class
'''
class BankAC:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        self. __balance += amount
    def get_balance(self):
        return self.__balance
Acc = BankAC(20000)
Acc.deposit(8000)
print(Acc.get_balance())
'''

#Inheritance--->This allows a child class(subclass) to acquire the attributes and methods of a parent class(Base Class)
#1.single inheritance--->Using single method of the class from parent class is know as single class parent:
#super()--->Used to call methods of the parent class from base class the child class
'''
class parent:
    def display(self):
        print("This is a parent method")
class child(parent):
    def display(self):
        super().display()
        print("This is child method")
obj = child()
obj.display()
'''

#2.Multiple Inheritance--->A child class inherits from more than one parent class
'''
class Father:
    def skill_1(self):
        print("Father: Hard working")
class Mother:
    def skill_2(self):
        print("Mother: Cooking")
class Child(Father, Mother):
    def All_skills(self):
        print("Child: Coding")
any = Child()
any.skill_1()
any.skill_2()
any.All_skills()
'''



    
