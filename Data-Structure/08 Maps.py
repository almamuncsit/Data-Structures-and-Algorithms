
import collections

my_dict = {'day1': 'Monday', 'day2': 'Tuesday'}
py_dict = {'day3': 'Wednesday', 'day1': 'Thursday'}

res = collections.ChainMap(my_dict, py_dict)

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


res2 = collections.ChainMap(py_dict, my_dict)
print(res2.maps, '\n')
