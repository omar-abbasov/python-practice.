import pandas as pd

data = {
    "well": ["Well-1", "Well-2", "Well-3", "Well-4", "Well-5", "Well-6"],
    "region": ["North", "South", "North", "South", "North", "South"],
    "depth": [3200, 2800, 4100, 3600, 2500, 3900],
    "pressure": [450, 380, 520, 410, 350, 490],
    "oil_rate": [120, 85, 210, 150, 60, 180]
}

df = pd.DataFrame(data)

# Среднее давление по регионам
print(df.groupby("region")["pressure"].mean())

# Максимальная добыча по регионам
print(df.groupby("region")["oil_rate"].max())

# Несколько метрик сразу
print(df.groupby("region")[["pressure", "oil_rate"]].agg(["mean", "max", "min"]))