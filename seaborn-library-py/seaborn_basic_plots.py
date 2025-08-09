# Basic Seaborn Plots

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = pd.DataFrame({
    'x': range(10),
    'y': [i**2 for i in range(10)],
    'category': ['A']*5 + ['B']*5
})

# Line plot
sns.lineplot(x='x', y='y', data=data)
plt.title('Basic Line Plot')
plt.show()

# Scatter plot
sns.scatterplot(x='x', y='y', hue='category', data=data)
plt.title('Scatter Plot with Hue')
plt.show()

# Bar plot
sns.barplot(x='category', y='y', data=data)
plt.title('Bar Plot')
plt.show()

# Histogram
sns.histplot(data['y'], bins=5, kde=True)
plt.title('Histogram with KDE')
plt.show()
