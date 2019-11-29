
if __name__ == '__main__':
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    print("dict['Name']: ", dict['Name'])
    print("dict['Age']: ", dict['Age'])

    dict['Age'] = 8  # update existing entry
    dict['School'] = "DPS School"  # Add new entry

    print("dict['School']: ", dict['School'])
    print("dict['Age']: ", dict['Age'])

    del dict['Name']
    print(dict)
