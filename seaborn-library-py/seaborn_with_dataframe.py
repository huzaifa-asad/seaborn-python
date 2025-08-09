# Seaborn with Pandas DataFrame

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create a DataFrame from a CSV (example)
# df = pd.read_csv('your_data.csv')

# For demonstration, use built-in dataset
df = sns.load_dataset('tips')

# Preview the DataFrame
print(df.head())

# Plot total bill vs tip, colored by time
sns.scatterplot(x='total_bill', y='tip', hue='time', data=df)
plt.title('Tips: Total Bill vs Tip by Time')
plt.show()

# Bar plot: average tip by day
sns.barplot(x='day', y='tip', data=df, estimator=pd.Series.mean)
plt.title('Average Tip by Day')
plt.show()
