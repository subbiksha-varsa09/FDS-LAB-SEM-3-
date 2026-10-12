import numpy as np
import pandas as pd

# Creating a DataFrame using a list
list1 = [[1, 'Smith', 50000], [2, 'Jones', 60000]]

df1 = pd.DataFrame(list1)
print(df1)

df1.columns = ['EmpId', 'Name', 'Salary']
print(df1)

# Display DataFrame information
print(df1.info())

# Reading a CSV file
df = pd.read_csv('employee.csv')

# Display first 5 rows
print(df.head())

# Display last 5 rows
print(df.tail())

# Display DataFrame information
print(df.info())

# Accessing the salary column
print(df.salary)

# Checking the data type
print(type(df.salary))

# Calculating statistical values
print(df.salary.mean())
print(df.salary.median())
print(df.salary.mode())
print(df.salary.var())
print(df.salary.std())

# Statistical summary
print(df.describe())

# Summary including all columns
print(df.describe(include='all'))

# Display column names
empCol = df.columns
print(empCol)

# Display DataFrame values
emparray = df.values
print(emparray)
