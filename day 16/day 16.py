import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
data = {
    "pressure": np.random.normal(430, 50, 100),
    "oil_rate": np.random.normal(130, 40, 100),
    "region": ["North"] * 50 + ["South"] * 50
}

df = pd.DataFrame(data)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Гистограмма
sns.histplot(data=df, x="pressure", bins=15,
             ax=axes[0])
axes[0].set_title("Pressure Distribution")

# KDE — сглаженная версия гистограммы
sns.kdeplot(data=df, x="pressure", hue="region",
            ax=axes[1])
axes[1].set_title("Pressure KDE by Region")

# Boxplot
sns.boxplot(data=df, x="region", y="oil_rate",
            ax=axes[2])
axes[2].set_title("Oil Rate Boxplot")

plt.tight_layout()
plt.savefig("day16_distributions.png")
plt.show()