'''#Ways to pass arguments in caling function

#required arguments- It should match same number variables in calling with def 

num = 9
num_2 = 10
def add(num, num_2):
    print(num, num_2)   #u can also print anyone in the given two and also add)
add (num, num_2)


#default arguments-it will take the default values from the arguments

My_name = "Kunnu"
def add(My_name):
    print(My_name)
add (My_name = "Srinivas")       #here Srinivas overwrites Kunnu
add (My_name = "Meghana")        #here Meghana is also printed because function is called 2nd time


#default arguments for prime numbers

num = 17
count= 0
def prime(num, count):
    for j in range(1, num+1):
        if num%j == 0:
            count+= 1
    if count == 2:
        print("prime")
    else:
        print("not a prime")        
prime(num,count)
prime(num=12,count=0)
    
    
def any(num, num_3, num_2):
    print(num_2, num, num_3)
any(num_2=21, num=0, num_3=95)


#variable length arguments- Adding a star(*) before the parameter name in the function, receive a tuple of arguments and can access items with indexes

def name(*Candidate_):
    print(Candidate_)
name("Kunnu", "Hari", "Karthi")'''
