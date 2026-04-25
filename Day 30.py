#File Handling --->A file handler is an object in file used to perform operations such as:creating,
#reading, writing, updating and deleting the file.
'''
#How to open a file
#1. open() ---> The open() function takes 2 parameters and in this after opening the file, we must close it using close() function after prfile name
#1)file name
#2)mode

#2. with open()---->Modes ("r","w","a","x","t")
#1."r"--read--->To read the file we use this mode and if the file does not exist, it throws an error.

file = open("dummy.txt","r")
print(file.read())
file.close()

#2."w"--write--->Used to write data into the file.It creates the file if it does not exist.If file exists, it overwrites the data.

file = open("dummy.txt","w")
file.write("I'm learning python")
file.close()

#3."a"--append--->Used to add the txt into the file without deleting existing data.It creates the file if it does not exist.It will write code at end

file = open("dummy.txt","a")
file.write("This is line 4")
file.close()

#4. "x"(create)->this is used to create the file, but this is already in the system it raise an error

To read a file
------------
#1.read()-->this method can read the entire file chunk by chunk
any = open("dummy.txt","r")
print(any.readline(1000))
any.close()

#2.readline()-->This method can only read one line at a time in a fi
any = open("dummy.txt","r")
print(any.readline(9))
any.close()

#3.readlines()-->This method can read the entire file and return into list with each line in one index in the list

any = open("dummy.txt","r")
print(any.read())
print(any.readline())
print(any.readlines())
any.close()


with open("dummy.txt","r") as any:
print(any.read())


