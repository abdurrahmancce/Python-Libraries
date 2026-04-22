import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'A': [1, 2, 3, 4],
    'B': [4, 3, 2, 1],
    'C': [5, 6, 7, 8]
}

df = pd.DataFrame(data)

# Heatmap
sns.heatmap(df.corr(), annot=True, cmap='Blues')

plt.title("Correlation Heatmap")
plt.show()