#Modules------->A module in a python is simply file that contain python code(Functions, Variable, Classes)
#To use modules, we have to use a keyword called import bef
#Types of Modules----> 1.Built-in or Inbuilt     2. User-define modules
#2.User-define module---> This is developed by the user or programmer inside a file of python code and used by called import with filename
#syntax---> import(keyword) file_name
#           file_name.functionality
'''

import module
print(module.add(7,4))
print(module.div(21,2))
print(module.sub(1991, 2002))
print(module.mul(14,7))
print(module.name)
print(module.square(91,20))
'''      


#1.Buitlt-in or Inbuilt---> Already these are comes with installation and are ready to use in the program
#This is developed by the developer
#Syntax--->import(keyword) module_name
#          module_name.functionality
'''

import math
print(math.sqrt(17))
'''


import random
num=random.randint(2,300)
attempts = 3
while attempts>0:
    user=int(input("Enter a number: "))
    if num==user:
         print("you won")
    else:
        attempts-= 1
        if attempts >0:
            print("Wrong, try again. Attempts left:", attempts)   
        else:
            print("You lose. The number was:", num)
