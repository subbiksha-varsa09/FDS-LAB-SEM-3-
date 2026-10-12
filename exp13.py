import pandas as pd
import numpy as np

# Read the dataset
data = pd.read_csv("Hotel.csv")

print("Original Dataset:")
print(data)

# Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:")
print(data[data.duplicated()])

# Remove duplicate records
data = data.drop_duplicates()

# Handle invalid ratings
data.loc[
    (data["Rating(1-5)"] < 1) | (data["Rating(1-5)"] > 5),
    "Rating(1-5)"
] = np.nan

# Handle invalid number of passengers
data.loc[data["NoOfPax"] < 0, "NoOfPax"] = np.nan

# Handle invalid salary
data.loc[data["EstimatedSalary"] < 0, "EstimatedSalary"] = np.nan

# Fill missing numerical values with mean
data["Rating(1-5)"] = data["Rating(1-5)"].fillna(
    data["Rating(1-5)"].mean()
)

data["NoOfPax"] = data["NoOfPax"].fillna(
    data["NoOfPax"].mean()
)

data["EstimatedSalary"] = data["EstimatedSalary"].fillna(
    data["EstimatedSalary"].mean()
)

# Correct hotel name
data["Hotel"] = data["Hotel"].replace("Ibys", "Ibis")

# Correct food preference
data["FoodPreference"] = data["FoodPreference"].replace({
    "Vegetarian": "Veg",
    "non-Veg": "Non-Veg"
})

# Display cleaned dataset
print("\nCleaned Dataset:")
print(data)

# Save cleaned dataset
data.to_csv("Cleaned_Hotel.csv", index=False)

print("\nCleaned dataset saved successfully!")