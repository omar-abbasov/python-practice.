import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "month": [1, 2, 3, 4, 5, 6],
    "oil_rate_north": [120, 135, 128, 142, 150, 145],
    "oil_rate_south": [85, 90, 88, 95, 102, 98]
}

df = pd.DataFrame(data)

plt.figure(figsize=(9, 4))

sns.lineplot(x="month", y="oil_rate_north",
             data=df, label="North", marker="o")
sns.lineplot(x="month", y="oil_rate_south",
             data=df, label="South", marker="o")

plt.title("Monthly Oil Rate by Region")
plt.xlabel("Month")
plt.ylabel("Oil Rate (bbl/day)")
plt.legend()
plt.tight_layout()
plt.savefig("day14_lines.png")
plt.show()