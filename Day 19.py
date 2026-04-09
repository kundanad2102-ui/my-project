'''
#lamba function
#this is also called anonymus function
# A lambda function can take n number of arguments but have only one expression

syntax---- lambda(keyword) arguments : expression


any = lambda so : so + 10
print(any(8))


some = lambda an,why,it : (why-an)*it    #there can be n of arguments but only one expression can be passed
print(some(5, 11, 5))


they = lambda how,are,you : (you/how)
print(they(9,5,13))


whom = lambda are,was : (was-are)
print(whom(17,8))


when = lambda a,am : (am+a)
print(when(3,6))


what = lambda she,he : (she*he)
print(what(3,8))


#List Comprehension:
#this is offers the shorter syntax when you want to create a new list from the exixting list

syntax----- Variable_name =  [expression loop condition]


old_list = [2,4,5,6,7]
new_list = [j for j in old_list if j%2==0]
print(new_list)
'''
