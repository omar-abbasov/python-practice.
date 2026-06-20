import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "well": ["Well-1", "Well-2", "Well-3",
             "Well-4", "Well-5", "Well-6"],
    "region": ["North", "South", "North",
               "South", "North", "South"],
    "depth": [3200, 2800, 4100, 3600, 2500, 3900],
    "pressure": [450, 380, 520, 410, 350, 490],
    "oil_rate": [120, 85, 210, 150, 60, 180]
}

df = pd.DataFrame(data)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Bar chart — средняя добыча по регионам
sns.barplot(data=df, x="region", y="oil_rate",
            ax=axes[0])
axes[0].set_title("Average Oil Rate by Region")

# Scatter — глубина vs давление, цвет по региону
sns.scatterplot(data=df, x="depth", y="pressure",
                hue="region", s=150, ax=axes[1])
axes[1].set_title("Depth vs Pressure by Region")

plt.tight_layout()
plt.savefig("day15_charts.png")
plt.show()