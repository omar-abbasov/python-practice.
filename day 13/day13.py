import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "well": ["Well-1", "Well-2", "Well-3", "Well-4", "Well-5", "Well-6"],
    "region": ["North", "South", "North", "South", "North", "South"],
    "depth": [3200, 2800, 4100, 3600, 2500, 3900],
    "pressure": [450, 380, 520, 410, 350, 490],
    "oil_rate": [120, 85, 210, 150, 60, 180]
}

df = pd.DataFrame(data)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# График 1 — boxplot давления по регионам
sns.boxplot(data=df, x="region", y="pressure", ax=axes[0])
axes[0].set_title("Pressure by Region")

# График 2 — heatmap корреляций
corr = df[["depth", "pressure", "oil_rate"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=axes[1])
axes[1].set_title("Correlation Heatmap")

# График 3 — scatter с цветом по региону
sns.scatterplot(data=df, x="depth", y="oil_rate",
                hue="region", s=100, ax=axes[2])
axes[2].set_title("Depth vs Oil Rate by Region")

plt.tight_layout()
plt.savefig("day13_seaborn.png")
plt.show()