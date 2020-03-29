days_set = set(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
months_set = {"Jan", "Feb", "Mar"}
dates_set = {21, 22, 17}
print(days_set)
print(months_set)
print(dates_set)

days_set = set(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
days_set.add("Sunday")
print(days_set)

days_set.discard("Sunday")
print(days_set)

print("Union of Sets")
days_setA = set(["Monday", "Tuesday", "Wednesday"])
days_setB = set(["Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
all_days_set = days_setA | days_setB
print(all_days_set)

print("Union of Sets")
all_days_set = days_setA & days_setB
print(all_days_set)

print('Difference')
all_days_set = days_setA - days_setB
print(all_days_set)

all_days_set = days_setB - days_setA
print(all_days_set)
