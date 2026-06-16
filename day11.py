import pandas as pd
import matplotlib.pyplot as plt

data = {
    "well": ["Well-1", "Well-2", "Well-3", "Well-4", "Well-5"],
    "depth": [3200, 2800, 4100, 3600, 2500],
    "pressure": [450, 380, 520, 410, 350],
    "oil_rate": [120, 85, 210, 150, 60]
}

df = pd.DataFrame(data)

# График 1 — линейный
plt.figure(figsize=(8, 4))
plt.plot(df["well"], df["pressure"], marker="o", color="steelblue")
plt.title("Pressure by Well")
plt.xlabel("Well")
plt.ylabel("Pressure (psi)")
plt.tight_layout()
plt.savefig("pressure_chart.png")
plt.show()

# График 2 — bar chart
plt.figure(figsize=(8, 4))
plt.bar(df["well"], df["oil_rate"], color="darkorange")
plt.title("Oil Rate by Well")
plt.xlabel("Well")
plt.ylabel("Oil Rate (bbl/day)")
plt.tight_layout()
plt.savefig("oilrate_chart.png")
plt.show()