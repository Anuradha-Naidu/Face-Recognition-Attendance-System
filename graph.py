import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('bmh')
df = pd.read_csv('anuradha.csv')

x = df['Roll']
y = df['Teacher']

plt.xlabel('Roll',fontsize=18)
plt.ylabel('Teacher',fontsize=16)
plt.bar(x,y)

plt.show()