import pandas as pd

pd.options.display.max_columns = 10
# Creating a variable named df (Standing for DataFrame) and reading the CSV file data with Pandas.
df = pd.read_csv('SampleData.csv')
# The Pandas .describe method returns a table of statistics about our data.
print(df.describe())
# Pandas .head method prints just the first 5 lines of data in a DataFrame.
# Pandas .tail method prints just the last 5 lines of data in a DataFrame.
print(df.head())
print(df.tail())
