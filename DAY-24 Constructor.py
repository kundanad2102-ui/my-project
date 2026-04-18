#Constructor(__init__)-----> A constructor is a special method used to initialize the object data that is __init__()
'''
class books:                                 
    def __init__(self, name, author):             
        self.name= name
        self.author= author
    def display(self):
        print(books_1.name, books_1.author)
        print(books_2.name, books_2.author)
books_1 = books("Chetan Bhagat", "Half Girlfriend")
books_2 = books("Sagar Chudesara", "We are there for each other")
books_1.display()
books_2.display()
'''

#Access specifiers----> 1.Public 2.Protected 3.Private
#1.Public: syntax -- name
#we can use it anywhere in the program
#2.Protected: syntax -- _name
#this is only for internal use
#3.Private: syntax -- __name
#this one is restricted
#self---> This keyword is instance variable and unique for each object

class some:
    def __init__(self):
        self.public = "Public"
        self.protected = "Protected"
        self.private = "Private"
any = some()
print(any.public)
print(any._protected)
print(any.__private)



