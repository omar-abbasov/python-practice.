fruits=["apple","banana","cherry"]

for fruit in fruits:
    print(fruit)

numbers=[1,2,3,4,4]
print(sum(numbers))
print(max(numbers))

# Словарь — данные о скважине
well={
    "Name":"Well-1",
    "depth": 3200,
    "pressure": 450,
    "active": True
    }
well["location"]="Baku"
for key,value in well.items():
    print("{}:{}".format(key,value))