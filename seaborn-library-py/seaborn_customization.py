# Seaborn Customization Examples

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Set theme
sns.set_theme(style="darkgrid")

# Sample data
data = pd.DataFrame({
    'x': range(10),
    'y': [i**1.5 for i in range(10)]
})

# Custom palette
palette = sns.color_palette("mako", as_cmap=True)

# Line plot with customizations
sns.lineplot(x='x', y='y', data=data, color='red')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.title('Customized Line Plot')
plt.show()

# Bar plot with palette
sns.barplot(x='x', y='y', data=data, palette="Blues")
plt.title('Bar Plot with Custom Palette')
plt.show()
