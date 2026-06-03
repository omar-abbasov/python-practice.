import random

well_pressures = [random.randint(300, 600) for _ in range(10)]

print("Все значения:", well_pressures)
print("Максимум:", max(well_pressures))
print("Минимум:", min(well_pressures))
print("Среднее:", sum(well_pressures) / len(well_pressures))
