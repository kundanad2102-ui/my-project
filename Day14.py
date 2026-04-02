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
