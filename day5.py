import pandas as pd

data={"well":["Well-1", "Well-2","Well-3", "Well-4"],
              "depth":[3200, 2800, 4100, 3600]
              ,"pressure":[450, 380, 520, 410],
              "active":[True, False, True, True]}

df=pd.DataFrame(data)

print(df)

print('---')
print('Среднее давление:',df['pressure'].mean())
print('Самая глубокая скважина:',df['depth'].max())

