import pandas as pd

data = {
    "well": ["Well-1", "Well-2", "Well-3", "Well-4", "Well-5"],
    "depth": [3200, 2800, 4100, 3600, 2500],
    "pressure": [450, 380, 520, 410, 350],
    "oil_rate": [120, 85, 210, 150, 60]
}

df = pd.DataFrame(data)

# Описательная статистика
print(df.describe())

# Нормализация давления — приводим к диапазону 0-1
df["pressure_normalized"] = (df["pressure"] - df["pressure"].min()) / (df["pressure"].max() - df["pressure"].min())

print("\nС нормализацией:")
print(df)