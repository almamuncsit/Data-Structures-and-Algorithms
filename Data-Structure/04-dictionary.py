
if __name__ == '__main__':
    pyt_dict = {'name': 'Mamun Sarkar', 'age': 26, 'class': 'First class'}
    print("pyt_dict['name']: ", pyt_dict['name'])
    print("pyt_dict['age']: ", pyt_dict['age'])

    pyt_dict['age'] = 8  # update existing entry
    pyt_dict['School'] = "DPS School"  # Add new entry

    print("pyt_dict['School']: ", pyt_dict['School'])
    print("pyt_dict['age']: ", pyt_dict['age'])

    del pyt_dict['name']
    print(pyt_dict)
