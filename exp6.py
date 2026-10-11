import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

data = pd.read_csv(
    "website_traffic.csv",
    parse_dates=["Date"],
    index_col="Date"
)

print("First five rows:")
print(data.head())

print("\nMissing values:")
print(data.isnull().sum())

data = data.interpolate()

decomposition = seasonal_decompose(
    data["Page_Views"],
    model="additive",
    period=7
)

decomposition.plot()

plt.suptitle(
    "Time Series Decomposition of Page Views",
    fontsize=14
)

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(data.index, data["Page_Views"])
plt.title("Website Page Views")
plt.xlabel("Date")
plt.ylabel("Page Views")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(data.index, data["Unique_Visitors"])
plt.title("Unique Visitors Over Time")
plt.xlabel("Date")
plt.ylabel("Unique Visitors")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(data.index, data["Bounce_Rate"])
plt.title("Bounce Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Bounce Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

data["Page_Views_MA"] = data["Page_Views"].rolling(
    window=7
).mean()

plt.figure(figsize=(10, 5))

plt.plot(
    data.index,
    data["Page_Views"],
    label="Page Views"
)

plt.plot(
    data.index,
    data["Page_Views_MA"],
    label="7-Day Moving Average"
)

plt.title("Page Views with Moving Average")
plt.xlabel("Date")
plt.ylabel("Page Views")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

data["Page_Views_Z"] = (
    (data["Page_Views"] - data["Page_Views"].mean())
    / data["Page_Views"].std()
)

anomalies = data[
    data["Page_Views_Z"].abs() > 2
]

print("\nDetected Anomalies:")
print(anomalies[["Page_Views", "Page_Views_Z"]])

plt.figure(figsize=(10, 5))

plt.plot(
    data.index,
    data["Page_Views"],
    label="Page Views"
)

plt.scatter(
    anomalies.index,
    anomalies["Page_Views"],
    color="red",
    label="Anomalies"
)

plt.title("Website Traffic Anomaly Detection")
plt.xlabel("Date")
plt.ylabel("Page Views")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()