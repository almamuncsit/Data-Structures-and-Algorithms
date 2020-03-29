from numpy import *

my_arr = array([['Mon', 18, 20, 22, 17], ['Tue', 11, 18, 21, 18],
           ['Wed', 15, 21, 20, 19], ['Thu', 11, 20, 22, 21],
           ['Fri', 18, 17, 23, 22], ['Sat', 12, 22, 20, 18],
           ['Sun', 13, 15, 19, 16]])

matrix = reshape(my_arr, (7, 5))
print(matrix)

# Print data for Wednesday
print(matrix[2])
# Print data for friday evening
print(matrix[4][3])

matrix_r = append(matrix, [['Avg', 12, 15, 13, 11]], 0)
print(matrix_r)

matrix_c = insert(matrix, [5], [[1], [2], [3], [4], [5], [6], [7]], 1)
print(matrix_c)

print("Before Delete")
print(matrix)
matrix = delete(matrix, [2], 0)
print('After Delete')
print(matrix)

matrix = delete(matrix, s_[2], 1)
print(matrix)

matrix[3] = ['Thu', 0, 0, 0]
print(matrix)
