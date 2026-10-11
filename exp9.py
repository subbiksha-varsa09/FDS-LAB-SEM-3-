import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load Iris Dataset
data = pd.read_csv("Iris_Dataset.csv")

# Display the dataset
print(data)

# Display information about the dataset
print("\nDataset Information:")
data.info()

# Statistical description
print("\nStatistical Description:")
print(data.describe())

# Count each variety
print("\nVariety Count:")
print(data.value_counts("variety"))

# Count Plot
sns.countplot(x="variety", data=data)
plt.show()

# Convert variety into dummy variables
dummies = pd.get_dummies(data["variety"])

# Create Final Dataset
FinalDataset = pd.concat(
    [dummies, data.iloc[:, [0, 1, 2, 3]]],
    axis=1
)

# Display first 5 rows
print("\nFinal Dataset:")
print(FinalDataset.head())

# Scatter Plot - Sepal
sns.scatterplot(
    x="SepalLengthCm",
    y="SepalWidthCm",
    hue="variety",
    data=data
)
plt.show()

# Scatter Plot - Petal
sns.scatterplot(
    x="PetalLengthCm",
    y="PetalWidthCm",
    hue="variety",
    data=data
)
plt.show()

# Pair Plot
sns.pairplot(
    data,
    hue="variety",
    height=3
)
plt.show()

# Histogram - Petal Length
sns.histplot(
    data=data,
    x="PetalLengthCm",
    hue="variety"
)
plt.show()

# Histogram - Petal Width
sns.histplot(
    data=data,
    x="PetalWidthCm",
    hue="variety"
)
plt.show()

# Histogram - Sepal Length
sns.histplot(
    data=data,
    x="SepalLengthCm",
    hue="variety"
)
plt.show()