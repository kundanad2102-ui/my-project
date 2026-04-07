#function()--->a function is a block of code which is reusable.these are of 2 types:built-in and user-defined
#built-in--->comes with the program and are already defined.ex-print(),sum(),map()
#user-defined--->created by person who is developing or using for development.starts with def keyword followed by function name
#and it has calling function.
'''
def fun_name():  #the variables passed in () are called parameters
   .......
   .......
   .......
fun_name()       #here they are called arguements but the elements are same
'''
#odd or even
'''
num=10
def num_odd_even(num):
    if num%2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
num_odd_even(num)
'''
'''
num=10
def num_odd_even(num):
    if num%2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
num_odd_even(num=2)                    #arguements value can be changed and it considers this arguement value only
'''
num=int(input("enter a number: "))
count=0
def prime_or_not(num,count):                  #(n,k) any name can be given here
    for i in range(1,num+1):                         #but names inside the fun also have to be changed.(1,n+1)
        if num%i==0:                                #n%i==0
            count+=1                                 #k+=1
    if count==2:                                       #k==2
        print("prime")
    else:
        print("not")
prime_or_not(num,count)                       #only the intialised names have to be given here
