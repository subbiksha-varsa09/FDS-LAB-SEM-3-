import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Date": [
        "2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04",
        "2023-01-05", "2023-01-06", "2023-01-07", "2023-01-08",
        "2023-01-09", "2023-01-10", "2023-01-11", "2023-01-12",
        "2023-01-13", "2023-01-14", "2023-01-15", "2023-01-16"
    ],
    "Product": [
        "Product A", "Product B", "Product A", "Product C",
        "Product B", "Product A", "Product C", "Product B",
        "Product A", "Product C", "Product B", "Product A",
        "Product C", "Product B", "Product A", "Product C"
    ],
    "Sales": [
        200, 150, 220, 300,
        180, 250, 320, 170,
        230, 310, 190, 210,
        340, 160, 240, 290
    ],
    "Quantity": [
        4, 3, 5, 6,
        4, 6, 7, 3,
        5, 7, 4, 5,
        8, 3, 5, 7
    ],
    "Region": [
        "North", "South", "North", "East",
        "West", "North", "East", "South",
        "North", "East", "West", "North",
        "East", "South", "North", "West"
    ]
}

df = pd.DataFrame(data)

# Save as CSV
df.to_csv("sales-data.csv", index=False)

print("sales-data.csv created successfully!")
print(df)


file_path = "sales-data.csv"
df = pd.read_csv(file_path)

print("First 5 rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

df["Sales"] = df["Sales"].fillna(df["Sales"].mean())

df = df.dropna(subset=["Product", "Quantity", "Region"])

print("\nSummary Statistics:")
print(df.describe())

product_summary = df.groupby("Product").agg({
    "Sales": "sum",
    "Quantity": "sum"
}).reset_index()

print("\nProduct Summary:")
print(product_summary)

plt.figure(figsize=(10, 6))

plt.bar(
    product_summary["Product"],
    product_summary["Sales"]
)

plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.title("Total Sales by Product")
plt.show()

df["Date"] = pd.to_datetime(df["Date"])

sales_over_time = df.groupby("Date").agg({
    "Sales": "sum"
}).reset_index()

plt.figure(figsize=(10, 6))

plt.plot(
    sales_over_time["Date"],
    sales_over_time["Sales"],
    marker="o"
)

plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.title("Sales Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

pivot_table = df.pivot_table(
    values="Sales",
    index="Region",
    columns="Product",
    aggfunc="sum",
    fill_value=0
)

print("\nPivot Table:")
print(pivot_table)

correlation_matrix = df[["Sales", "Quantity"]].corr()

print("\nCorrelation Matrix:")
print(correlation_matrix)

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Matrix")
plt.show()