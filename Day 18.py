#Recursive functions- Recursion is a programming technique where a function calls itsef either directly or indirectly to solve a problem by breaking
#it into smaller, simpler subproblems. Recursion is especially usefu for problems that can be divided into identical smaller tadsks, such as mathematical
#calculations, tree transversals or divide and conquer algorithms

'''def validate_pin(self):
    while self.remaining_attempts > 0:
        user_pin = input("Enter 4 digit PIN: ")
        if len(user_pin) == 4 and  user_pin == self.user_info["ATM PIN"]:
            print(" ✅Welcome to the ATM")
            return True
        else:
            self.remaining_attempts -= 1
            if self.remaining_attempts > 0:
                print(f"❌Invalid PIN. Attempts left: {self.remaining_attempts}")
            else:
                print("Card blocked. Please contact customer service")
                return False


any = "Python is a Language"
Vowel_list = []
Con_list = []
def Vowel_con(any, Vowel_list, Con_list):
    for j in any:
        if j in "AEIOUaeiou":
            Vowel_list.append(j)
        else:
            Con_list.append(j)
    print(f"{Vowel_list} these are all vowel in the string")
    print(f"{Con_list} these are all consonants in the string")
Vowel_con(any,Vowel_list,Con_list)'''

                
        
any = "Python is a Language"
Vowel_list = []
Con_list = []
def Vowel_con(any, Vowel_list, Con_list):
    for j in any:
        if j in "AEIOUaeiou":
            Vowel_list.append(j)
        elif j not in "AEIOUaeiou" and j not in " ":               #excludes spaces also
            Con_list.append(j)
    print(f"{Vowel_list} these are all vowel in the string")
    print(f"{Con_list} these are all consonants in the string")
Vowel_con(any,Vowel_list,Con_list)
        
        
        
