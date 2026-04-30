#BAR CHART
import matplotlib.pyplot as plt
plt.bar([2024,2025,2026],[67,89,50])
plt.title("Car Sales")
plt.xlabel("Years")
plt.ylabel("Number of Cars sold")
plt.show()

import matplotlib.pyplot as plt
plt.scatter([1,2,3,4],[200,400,100,800], color="Yellow", s=100)
plt.title("Swift Car Sales")
plt.xlabel("Years")
plt.ylabel("Number of Sales")
plt.show()

import matplotlib.pyplot as plt
plt.bar([2024,2025,2026],[67,89,50], 150, color="Gray")
plt.title("Car Sales")
plt.xlabel("Years")
plt.ylabel("Number of cars sold")
plt.show()    

import matplotlib.pyplot as plt
values = [40, 15, 35, 20]
labels = ["Backend (Python)","Frontend (HTML, CSS)","Framework (Flask)","Library (NumPy, Pandas, Matplotlib)"]
plt.pie(values, labels=labels)
plt.title("ATM Application (Project)")
plt.legend(["Sai", "Niral", "Abdul", "Teja"])
plt.show()










































