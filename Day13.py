#Table

table_num= int(input("Enter a number: "))
for j in range(1,11):
    print(f"{table_num} X {j} = { table_num * j}")
    

#Counting how many small and capital letters

an= "Python IS a programming Language"
count_U = 0
count_L = 0
for ch in an:
    if ch.isupper():
        count_U += 1
    elif ch.islower():
            count_L += 1
print(f"There are total {count_U} Cap L")
print(f"There are total {count_L} small L")


#capital separately and small letters separately

an= "Python IS a programming Lamguage"
Cap_L =[]
small_L = []
for ch in an:
    if ch.isupper():
        Cap_L.append(ch)
    elif  ch.islower():
        small_L.append(ch)
print(f"{Cap_L} contain all Cap L")
print(f"{small_L} contain all small L")


#ATM Pin

ICIC_kunnu_AC_details= {"Name" : "Kunnu",
                        "ATM PIN" : "2102"}
print("Welcome to ICIC ATM")
print("Pls inster your ATM card")
ICIC_user_pin = input("Pls enter your 4 digits ATM pin: ")
if len(ICIC_user_pin) == 4:
    if ICIC_user_pin in ICIC_kunnu_AC_details["ATM PIN"]:
        print("The pin correct")
    else:
        print("Please enter 4 digits PIN")

     
#Perfect number

per_num = int(input("Enter a number: "))
fact_all = 0
for j in range(1, per_num):
    if per_num % j == 0:
        fact_all += j
if fact_all == per_num:
    print(f"{per_num} is the perfect num")
else:
    print(f"{per_num} is not a perfect num")
    
        
