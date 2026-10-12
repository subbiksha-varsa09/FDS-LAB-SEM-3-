import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# LOAD DATASET
tips = sns.load_dataset('tips')

# BASIC EDA
print(tips.head())
print(tips.tail())
print(tips.shape)
print(tips.columns)
print(tips.info())
print(tips.describe())

# MISSING VALUES
print(tips.isnull().sum())

# DUPLICATE VALUES
print(tips.duplicated().sum())

# UNIQUE VALUES
print(tips.nunique())

# VALUE COUNTS
print(tips['sex'].value_counts())
print(tips['smoker'].value_counts())
print(tips['day'].value_counts())
print(tips['time'].value_counts())

# CORRELATION
print(tips.corr(numeric_only=True))

# DISTRIBUTION PLOT
sns.displot(tips['total_bill'], kde=True)
plt.show()

# JOINT PLOT
sns.jointplot(x='tip', y='total_bill', data=tips)
plt.show()

# PAIR PLOT
sns.pairplot(tips)
plt.show()

# PAIR PLOT WITH HUE
sns.pairplot(tips, hue='time')
plt.show()

# HEATMAP
sns.heatmap(tips.corr(numeric_only=True), annot=True)
plt.show()

# BOX PLOT
sns.boxplot(x=tips['total_bill'])
plt.show()

sns.boxplot(x=tips['tip'])
plt.show()

# COUNT PLOT
sns.countplot(x='day', data=tips)
plt.show()

sns.countplot(x='sex', data=tips)
plt.show()

# PIE CHART
tips['sex'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.show()

# BAR CHART
tips['sex'].value_counts().plot(kind='bar')
plt.show()

# FILTERED ANALYSIS
sns.countplot(x=tips[tips['time'] == 'Dinner']['day'])
plt.show()