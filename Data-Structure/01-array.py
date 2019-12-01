from array import *

array1 = array('i', [1, 4, 5, 6, 3, 8])
array1.insert(1, 60)

for item in array1:
    print(item)

array1.remove(3)

print(array1)
print(array1.index(6))

array1[2] = 80
print(array1)
