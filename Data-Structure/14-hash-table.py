# Declare a hashtable using dictionary
hash_table = {'name': 'Mamun', 'age': 26, 'class': 'First Class'}

# Accessing the dictionary with its key
print("hash_table['name']: ", hash_table['name'])
print("hash_table['age']: ", hash_table['age'])


hash_table['age'] = 8  # update existing entry
hash_table['School'] = "DPS School"  # Add new entry
print("hash_table['age']: ", hash_table['age'])
print("hash_table['School']: ", hash_table['School'])

print(hash_table)
del hash_table['name']  # remove entry with key 'name'
print(hash_table)
hash_table.clear()  # remove all entries in hash_table
print(hash_table)
del hash_table  # delete entire dictionary
