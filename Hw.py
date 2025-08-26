import pandas as pd

# Load data from a CSV file
df = pd.read_csv('n.csv')

# Display the first 5 rows
print(df.head(5))

# Get a summary of the data and data types
df.info()
# Get descriptive statistics for numerical columns
df.describe()
import matplotlib.pyplot as plt

# Create a line plot of a single column
df['no'].plot(kind='line')
plt.show()

# Create a scatter plot to show the relationship between two variables
df.plot.scatter(x='x_axis_column', y='y_axis_column')
plt.show()    