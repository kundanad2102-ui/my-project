#pattern programs

num = int(input())
for j in range(num):
    for i in range(j):
        print("*", end ="")    #end is used to print * side by side
    print()                    #to end the line


num = int(input("Enter the limit:"))
for j in range(num):
    for i in range(j):
        print (j, end ="")
    print()


num = int(input("Enter the limit:"))
for j in range(num):
    for i in range(j):
        print (i, end ="")
    print()

   
num = int(input())
for j in range(num):
    for i in range(num):
        print("*", end ="")
    print()


num = int(input("Enter the limit:"))
for j in range(num):
    for i in range(num-j):
        print("*", end ="")
    print()


num = int(input("Enter the limit:"))
for j in range(num+1):
    for i in range(1,j+1):
        print(i, end ="")
    print()


num = int(input("Enter the limit:"))
for j in range (num):
    print(" " *(num-j), end = "")
    for i in range(j+1):
        print("*", end ="")
    print()


num = int(input("Enter the limit:"))
for j in range (num):
    print(" " *(num-j), end ="")
    for i in range(j+1):
        print("*", end =" ")
    print()

