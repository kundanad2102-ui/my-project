'''
#Generators----->This is a special type of function that return an ITERATOR which one at a time(slight time delay)
#yield--->It will take a pause and again resume, this is not a npormal keyword cannot be ised in the normal functions
#used to produce a value and pause execution

def gen():      
    yield 1      #yield is similar to yield in functions
    yield 2
    yield 3
my = gen()
print(next(my))
print(next(my))
print(next(my))'''


'''
def square_gen(n):
    for i in range(n):
        yield i*i
for val in square_gen(8):
    print(val)'''


'''
def add(n,m):
    yield n+m
my = add(14,21)
print(next(my))'''


'''
def num():
    if n%2==0:
        yield 'even'
    else:
        yield 'odd'
my= num()
print(next(my))'''


'''
#Next()---->This is used to get value from a generator
#when the value is finished, it will stop the iterator
def square_gen(n):
    for i in range(n):
        yield i
for val in square_gen(11):
    print(val)'''
