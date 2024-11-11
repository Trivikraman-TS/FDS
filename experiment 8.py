import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("d://Trivikraman//FLEX PORT//TECHNICAL//people.csv")
print(data.head(10))
deta=data.head(10)

plt.scatter(deta['Name'], deta['Height(cm)'])
plt.title('Scatter Plot')
plt.xlabel('Name')
plt.xlabel('Height(in cm)')
plt.show()