'''#Break

#when break is used to exit from the loop, when we found the required value

for j in range(1, 10):
    print(j)
    if j == 5:
        break


#inlists

lis_ = [1,2,3,4]
for n in lis_:
    print(n)
    if n == 1:
        break


#continue is used to skip the particular loop

for j in range(1,10):
    if j == 5:
        continue
    print(j)

lis_ = [11,12,13,14]
for n in lis_:
    if n == 13:
        continue
    print(n)


#pass is called a space holder incase any statement like(if, for, else, elif...) this should complete, if not we will get indentation error to
#avoid this we are using pass

for j in range(1,100):
    pass



#else for forloop- it will fall back to else blaock, when all loops are completed

for m in range(1,10):
    print(m)
else:
    print("else block")


#while loop is a combination of for and if statements, if we did not end the loop in  proper way it will run upto the memory space until it becomes empty

num = 1
while num<5:
    print(num)   #it will give continues output 1 

num = 1
while num<5:
    print (num)
    num += 1


#generating fibonacci series with python

user_int = int(input(" Enter the limit:"))
num_1 = 0
num_2 = 1
print( num_1, num_2)
for v in range(user_int+1):
    pass                      #loop1

user_int = int(input(" Enter the limit:"))
num_1 = 0
num_2 = 1
print( num_1, num_2)
for v in range(user_int+1):
    num_3 = num_1+ num_2
    print(num_3, end= " ")     #loop2

user_int = int(input(" Enter the limit:"))
num_1 = 0
num_2 = 1
print( num_1, num_2)
for v in range(user_int+1):
    num_3 = num_1+ num_2
    num_1 = num_2
    num_2 = num_3
    print(num_3, end= " ")     #loop3'''

