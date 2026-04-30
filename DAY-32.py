'''
#User Registration Validation Program
import re
def validate_name(name):
    pattern = r'^[A-Za-z]{3,}$'
    return re.fullmatch(pattern, name)

def validate_email(email):
    pattern = r'^[\w.-]+@[\w.-]+\.\w+$'
    return re.fullmatch(pattern, email)

def validate_phone(phone):
    pattern = r'^[0-9]{10}$'
    return re.fullmatch(pattern, phone)

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
    return re.fullmatch(pattern, password)

def main():
    name = input("Enter Name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    password = input("Enter password: ")

    if not validate_name(name):
        print("Invalid_Name")
    elif not validate_email(email):
        print("Invalid email")
    elif not validate_phone(phone):
        print("Invalid phone")
    elif not validate_password(password):
        print("Invalid password")
    else:
        print("All inputs are valid")
if __name__ == "__main__":
    main()
'''

'''
#DATA ANALYSIS
#Why this is need?---->This is critical bcoz it converts raw data into actionable insights, enabling information
#to decision-making easy and improve operational....
1.Decision-making
2.Improved Operational Efficiency
3. Customer Understanding
4. Market Insight
5. Risk Management
6. Data-Driven Strategies

pip install matplotlib
'''

'''
#LINE Graph
import matplotlib.pyplot as pit
X = [1,2,3,4,5]
Y = [10,20,15,25,9]
pit.plot(X,Y)
pit.show()

#BAR Graph
import matplotlib.pyplot as pit
pit.bar(["TV9","NDTV","SumanTV"],[4,10,7])
pit.show()

#PIE Graph
import matplotlib.pyplot as pit
pit.pie([30, 40, 20], labels = ["Kunnu", "Hari", "Karthee"])
pit.show()

#HISTOGRAM 
import matplotlib.pyplot as pit
pit.hist([23, 15, 78, 12])
pit.show()
'''

'''
#NUMPY---> Numpy(Numerical Python) is the fondational open-source library for scientific computing in python,
#providing high performance, N-dimensional array objects(ndarray)
#This enables efficient numerical computation linear algebra, and data manipulation, serving as the basis
#for the tools like Tensorflow and scipy

pip install NumPY
'''

'''
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y)
plt.show()
'''

'''
#PANDAS--->This pandas is used for handling structured data in table format

pip install pandas
'''

'''
import pandas as pd
data = {"Name" : ["Sangeetha", "Vidhya"], "Marks" : [35, 89,]}
any = pd.DataFrame(data)
print(any)
'''




   
