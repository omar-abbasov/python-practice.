import pandas as pd
import numpy as np

data = {
    "well": ["Well-1", "Well-2", "Well-3", "Well-4", "Well-5"],
    "depth": [3200, np.nan, 4100, 3600, np.nan],
    "pressure": [450, 380, np.nan, 410, 350],
    "oil_rate": [120, 85, 210, np.nan, 60]
}

df = pd.DataFrame(data)

# Где пропуски?
print(df.isnull().sum())

# Заполнить средним
df["depth"] = df["depth"].fillna(df["depth"].mean())
df["pressure"] = df["pressure"].fillna(df["pressure"].median())

# Удалить строки где остались пропуски
df = df.dropna()

print("\nПосле очистки:")
print(df)

# Сохранить чистый датасет
df.to_csv("clean_wells.csv", index=False)
print("\nСохранено в clean_wells.csv")