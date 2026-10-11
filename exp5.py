import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

diabetes_df = pd.read_csv("diabetes.csv")

print("First five rows:")
print(diabetes_df.head())

print("\nLast five rows:")
print(diabetes_df.tail())

print("\nShape of the dataset:")
print(diabetes_df.shape)

print("\nColumn names:")
print(diabetes_df.columns)

print("\nDataset Information:")
diabetes_df.info()

print("\nMissing Values:")
print(diabetes_df.isnull().sum())

print("\nStatistical Summary:")
print(diabetes_df.describe())