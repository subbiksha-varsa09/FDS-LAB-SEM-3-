import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)  # To get the same result every time

# Step 1: Create the population of 10,000 students
population = np.random.normal(loc=65, scale=12, size=10000).round()
population = np.clip(population, 0, 100)  # Keep marks between 0 and 100

# Step 2: Draw a random sample of 50 students
sample = np.random.choice(population, size=50, replace=False)

# Step 3: Calculate population parameters and sample statistics
print("POPULATION (N = 10000)")
print(f"Population mean (mu) = {population.mean():.2f}")
print(f"Population SD (sigma) = {population.std():.2f}")

print("\nSAMPLE (n = 50)")
print(f"Sample mean (x-bar) = {sample.mean():.2f}")
print(f"Sample SD (s) = {sample.std(ddof=1):.2f}")

print(f"Sampling error (x-bar - mu) = {sample.mean() - population.mean():.2f}")

# Step 4: Calculate means of 5 different random samples
print("\nMeans of 5 different random samples of size 50:")

for i in range(1, 6):
    s = np.random.choice(population, size=50, replace=False)
    print(f"Sample {i}: mean = {s.mean():.2f}")

# Step 5: Plot population and sample histograms
fig, ax = plt.subplots(1, 2, figsize=(12, 4))

# Population histogram
ax[0].hist(population, bins=30, color="skyblue", edgecolor="black")
ax[0].axvline(
    population.mean(),
    color="red",
    linestyle="--",
    label=f"Population mean = {population.mean():.1f}"
)
ax[0].set_title("Population: Marks of 10,000 Students")
ax[0].set_xlabel("Marks")
ax[0].set_ylabel("Number of students")
ax[0].legend()

# Sample histogram
ax[1].hist(sample, bins=10, color="orange", edgecolor="black")
ax[1].axvline(
    sample.mean(),
    color="green",
    linestyle="--",
    label=f"Sample mean = {sample.mean():.1f}"
)
ax[1].axvline(
    population.mean(),
    color="red",
    linestyle=":",
    label=f"Population mean = {population.mean():.1f}"
)
ax[1].set_title("Random Sample of 50 Students")
ax[1].set_xlabel("Marks")
ax[1].set_ylabel("Number of students")
ax[1].legend()

plt.tight_layout()
plt.show()
