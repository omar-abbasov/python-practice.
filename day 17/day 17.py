import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
pressures = np.random.normal(430, 50, 50)

mean = np.mean(pressures)
median = np.median(pressures)
std = np.std(pressures)
variance = np.var(pressures)

print(f"Mean:     {mean:.2f}")
print(f"Median:   {median:.2f}")
print(f"Std Dev:  {std:.2f}")
print(f"Variance: {variance:.2f}")

plt.figure(figsize=(8, 4))
plt.hist(pressures, bins=15, color="steelblue",
         edgecolor="white")
plt.axvline(mean, color="red",
            linestyle="--", label=f"Mean: {mean:.1f}")
plt.axvline(median, color="orange",
            linestyle="--", label=f"Median: {median:.1f}")
plt.title("Pressure Distribution - 50 Wells")
plt.xlabel("Pressure (psi)")
plt.ylabel("Count")
plt.legend()
plt.savefig("day17_stats.png")
plt.show()