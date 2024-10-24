import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV data
data = pd.read_csv('latency_results.csv')

# Create a boxplot
sns.boxplot(x='test_case', y='timestamp', data=data)
plt.title('API Latency Performance')
plt.ylabel('Time (seconds)')
plt.xlabel('Test Case')
plt.show()