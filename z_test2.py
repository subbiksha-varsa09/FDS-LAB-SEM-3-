
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Step 1: Given data
mu0 = 1000       # Claimed mean life
sigma = 100      # Population standard deviation
n = 50           # Sample size
x_bar = 975      # Sample mean
alpha = 0.05     # Significance level

# Step 2: Calculate Z statistic
z = (x_bar - mu0) / (sigma / np.sqrt(n))
print(f"Z statistic = {z:.4f}\n")

# Step 3: Two-tailed test
z_crit_two = stats.norm.ppf(1 - alpha / 2)
p_two = 2 * (1 - stats.norm.cdf(abs(z)))

print("TWO-TAILED TEST (H1: mu != 1000)")
print(f"Critical values = +/-{z_crit_two:.3f}, p-value = {p_two:.4f}")
print("Decision:", "Reject H0" if p_two < alpha else "Fail to reject H0")

# Step 4: Left-tailed test
z_crit_left = stats.norm.ppf(alpha)
p_left = stats.norm.cdf(z)

print("\nLEFT-TAILED TEST (H1: mu < 1000)")
print(f"Critical value = {z_crit_left:.3f}, p-value = {p_left:.4f}")
print("Decision:", "Reject H0" if p_left < alpha else "Fail to reject H0")

# Step 5: Right-tailed test
z_crit_right = stats.norm.ppf(1 - alpha)
p_right = 1 - stats.norm.cdf(z)

print("\nRIGHT-TAILED TEST (H1: mu > 1000)")
print(f"Critical value = {z_crit_right:.3f}, p-value = {p_right:.4f}")
print("Decision:", "Reject H0" if p_right < alpha else "Fail to reject H0")

# Step 6: Plot graphs
x = np.linspace(-4, 4, 500)
y = stats.norm.pdf(x)

fig, ax = plt.subplots(1, 2, figsize=(13, 4.5))

# Two-tailed test graph
ax[0].plot(x, y, "k", linewidth=2)
ax[0].fill_between(
    x, y, where=(x <= -z_crit_two),
    color="red", alpha=0.4,
    label="Rejection region (2.5% each)"
)
ax[0].fill_between(
    x, y, where=(x >= z_crit_two),
    color="red", alpha=0.4
)
ax[0].axvline(
    z, color="blue", linestyle="--",
    linewidth=2, label=f"Z = {z:.2f}"
)
ax[0].set_title(f"Two-tailed Test (p = {p_two:.3f})")
ax[0].set_xlabel("Z")
ax[0].set_ylabel("Probability Density")
ax[0].legend()

# Left-tailed test graph
ax[1].plot(x, y, "k", linewidth=2)
ax[1].fill_between(
    x, y, where=(x <= z_crit_left),
    color="red", alpha=0.4,
    label="Rejection region (5% left)"
)
ax[1].axvline(
    z, color="blue", linestyle="--",
    linewidth=2, label=f"Z = {z:.2f}"
)
ax[1].set_title(f"Left-tailed Test (p = {p_left:.3f})")
ax[1].set_xlabel("Z")
ax[1].set_ylabel("Probability Density")
ax[1].legend()

plt.tight_layout()
plt.show()
