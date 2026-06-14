import pandas as pd

wells_north = pd.DataFrame({
    "well": ["Well-1", "Well-2", "Well-3"],
    "region": ["North", "North", "North"],
    "oil_rate": [120, 210, 60]
})

wells_south = pd.DataFrame({
    "well": ["Well-4", "Well-5", "Well-6"],
    "region": ["South", "South", "South"],
    "oil_rate": [85, 150, 180]
})

# Объединить два датасета
all_wells = pd.concat([wells_north, wells_south], ignore_index=True)
print(all_wells)

# Таблица с дополнительными данными
pressure_data = pd.DataFrame({
    "well": ["Well-1", "Well-2", "Well-3", "Well-4", "Well-5", "Well-6"],
    "pressure": [450, 520, 350, 380, 410, 490]
})

# Merge — объединить по столбцу well
full_data = all_wells.merge(pressure_data, on="well")
print("\nПолные данные:")
print(full_data)