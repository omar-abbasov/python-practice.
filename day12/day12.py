import pandas as pd
import matplotlib.pyplot as plt

data = {
    "well": ["Well-1", "Well-2", "Well-3", "Well-4", "Well-5"],
    "depth": [3200, 2800, 4100, 3600, 2500],
    "pressure": [450, 380, 520, 410, 350],
    "oil_rate": [120, 85, 210, 150, 60]
}

df = pd.DataFrame(data)

# Два графика рядом
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

# Scatter — глубина vs давление
ax1.scatter(df["depth"], df["pressure"], color="steelblue", s=100)
ax1.set_title("Depth vs Pressure")
ax1.set_xlabel("Depth (m)")
ax1.set_ylabel("Pressure (psi)")

# Bar — добыча по скважинам
ax2.bar(df["well"], df["oil_rate"], color="darkorange")
ax2.set_title("Oil Rate by Well")
ax2.set_xlabel("Well")
ax2.set_ylabel("Oil Rate (bbl/day)")

plt.tight_layout()
plt.savefig("day12_charts.png")
plt.show()