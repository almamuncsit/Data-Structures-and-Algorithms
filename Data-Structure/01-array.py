from array import *

test_array = array('i', [10, 40, 50, 60, 30, 80])
test_array.insert(1, 600)

for item in test_array:
    print(item)

test_array.remove(30)

print(test_array)
print(test_array.index(60))

test_array[2] = 80
print(test_array)
