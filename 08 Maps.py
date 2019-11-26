
import collections

dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thu'}

res = collections.ChainMap(dict1, dict2)

# Creating a single dictionary
print(res.maps, '\n')

print('Keys = {}'.format(list(res.keys())))
print('Values = {}'.format(list(res.values())))
print()

print('elements:')
for key, val in res.items():
    print('{} = {}'.format(key, val))
print()


# Find a specific value in the result
print('day3 in res: {}'.format(('day3' in res)))
print('day4 in res: {}'.format(('day4' in res)))


res2 = collections.ChainMap(dict2, dict1)
print(res2.maps, '\n')
