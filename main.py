import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("heart.csv")

plt.scatter(data['Sex'], data['RestingBP'])

plt.title("Scatter Plot")

plt.xlabel('Sex')
plt.ylabel('RestingBP')

plt.show()