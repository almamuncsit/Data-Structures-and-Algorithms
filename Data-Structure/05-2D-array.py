
if __name__ == '__main__':
    test_2d_array = [[110, 120, 50, 20], [150, 60, 100], [100, 80, 120, 50], [120, 150, 80, 60]]
    test_2d_array.insert(2, [11, 50, 110, 130, 60])

    print(test_2d_array[0])
    print(test_2d_array[1][2])

    for r in test_2d_array:
        for c in r:
            print(c, end=" ")
        print()

    del test_2d_array[3]
    print(test_2d_array)
