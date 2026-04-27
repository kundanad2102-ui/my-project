#Regular expression(RegEx)---->This regular expression or RegEx is a sequence of characters that forms a searching pattern.
#T use this we have to import re, which will unlock the package
#Functions-- 1.Findall 2.search
'''
#1.Findall---> By using this function, it will find all the sequence in the string
syntax---> re.findall(metachar, variable_name)
import re
any = "Python is a language"
so = re.findall("a",any)

the = re.findall("h....o",we)
print(the)

import re
we = "hello"
thing = re.search("he..o",we)
print(thing)


#3.^ ---> This is used to find the string is starting with the sequence or not
#syntax-- re.findall("metacharacter",variable_name)
import re
how = "This is used to find the string is starting with the sequence or not"
who = re.findall("^This is",how)
print(who)

import re
how = "This is used to find the string is starting with the sequence or not"
then = re.search("^This",how)
print(then)


#4.$ ---> This is used to find the string is ending with sequence or not
#syntax-- re.findall("$",variable_name)
import re
out = "This is used to find the string is ending with sequence or not"
one = re.findall("sequence $",out)
print(one)

import re
out = "This is used to find the string is ending with sequence or not"
two = re.search("not$",out)
print(two)


#5.* ---> This will form a searching pattern as it will take any zero or more character for(*)
#syntax-- re.findall(".*",variable_name)
import re
kunnu = "This will form a searching pattern as it will take any zero or more character"
SK = re.findall("c.*i",kunnu)
print(SK)

import re
kunnu = "This will form a searching pattern as it will take any zero or more character"
DK = re.search("w.*",kunnu)
print(DK)


#6.+ ---> This meta character will form a searching pattern as it will take any one or more character for (+)
#syntax--> re.search(".+",variable_name)
import re
kunnu = "This meta character will form a searching pattern as it will take any one or more character"
SK = re.findall("an.+y",kunnu)
print(SK)

import re
kunnu = "This meta character will form a searching pattern as it will take any one or more character"
hari = re.search("T.*",kunnu)
print(hari)
'''





