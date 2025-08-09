import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample data for boxplot and violinplot
data = pd.DataFrame({
    'group': np.repeat(['A', 'B', 'C'], 30),
    'value': np.concatenate([
        np.random.normal(0, 1, 30),
        np.random.normal(2, 1.5, 30),
        np.random.normal(-1, 0.5, 30)
    ])
})

# Boxplot
sns.boxplot(x='group', y='value', data=data)
plt.title('Boxplot by Group')
plt.show()

# Violinplot
sns.violinplot(x='group', y='value', data=data)
plt.title('Violinplot by Group')
plt.show()

# Heatmap
corr = data.pivot_table(index='group', columns='value', aggfunc='size', fill_value=0)
sns.heatmap(corr, cmap='coolwarm')
plt.title('Heatmap Example')
plt.show()
