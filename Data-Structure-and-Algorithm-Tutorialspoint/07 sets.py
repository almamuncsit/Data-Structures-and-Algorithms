Days = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
Months = {"Jan", "Feb", "Mar"}
Dates = {21, 22, 17}
print(Days)
print(Months)
print(Dates)

Days = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"])
Days.add("Sun")
print(Days)

Days.discard("Sun")
print(Days)

print("Union of Sets")
DaysA = set(["Mon", "Tue", "Wed"])
DaysB = set(["Wed", "Thu", "Fri", "Sat", "Sun"])
AllDays = DaysA | DaysB
print(AllDays)

print("Union of Sets")
AllDays = DaysA & DaysB
print(AllDays)

print('Difference')
AllDays = DaysA - DaysB
print(AllDays)

AllDays = DaysB - DaysA
print(AllDays)
