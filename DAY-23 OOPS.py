#OOPs---> classes, objects,attributes,methods
#Object Oriented Language(OOP) is a style of programming where we model real-world things as objects
#that contain both data and functions()
#why oops?--> reusable of code, and also scalable
#Class---> Class is a blu print or template that defines what kind of data and behaviour a certain type of object will have
#Object---> Instance of class or an object is a real instance created from a class.It is the actual thing that exists in memory
#while the program runs
#Attributes---> These are variables that store data related to a class or object

'''
class dog:                             #dog=class
    def __init__(self, breed, name):    #breed,name=attributes
        self.breed= breed
        self.name= name
dog_1 = dog(" Siberian Husky", "Blue")   #dog_1,dog_2=objects
dog_2 = dog("Rottweiler", "Rocky")
print(dog_1.breed, dog_1.name)
print(dog_2.breed, dog_2.name)
'''

'''
class vegetables:                                 
    def __init__(self, colour, name):             
        self.colour= colour
        self.name= name
vegetables_1 = vegetables("Capsicum", "Yellow")   
vegetables_2 = vegetables("Carrot", "Orange")
print(vegetables_1.colour, vegetables_1.name)
print(vegetables_2.colour, vegetables_2.name)
'''

'''
class books:                                 
    def __init__(self, name, author):             
        self.name= name
        self.author= author
books_1 = books("Chetan Bhagat", "Half Girlfriend")   
books_2 = books("Sagar Chudesara", "We are there for each other")
print(books_1.name, books_1.author)
print(books_2.name, books_2.author)
'''

'''
class laptops:                                 
    def __init__(self, name, generation):             
        self.name= name
        self.generation= generation
laptops_1 = laptops("Apple Macbook Pro(M2)", "Apple Silicon 2nd gen")   
laptops_2 = laptops("Hp Pavilion 15", "Intel 11th gen")
print(laptops_1.name, laptops_1.generation)
print(laptops_2.name, laptops_2.generation)
'''

'''
class watches:                                 
    def __init__(self, brand, colour):             
        self.brand= brand
        self.colour= colour
watches_1 = watches("Michael Kors", "Gold")   
watches_2 = watches("Fossil", "Silver")
print(watches_1.brand, watches_1.colour)
print(watches_2.brand, watches_2.colour)    
'''

class companies:                                 
    def __init__(self, name, location):             
        self.name= name
        self.location= location
companies_1 = companies("Microsoft", "Hyderabad")   
companies_2 = companies("Deloitee", "Banglore")
print(companies_1.name, companies_1.location)
print(companies_2.name, companies_2.location)    
