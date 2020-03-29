def linear_search(items, val):
    length = len(items)
    for i in range(0, length):
        if items[i] == val:
            return i

    return None


# Initialize the sorted list
items = [2, 7, 11, 19, 34, 53, 3, 45, 72, 75]

# Print the search result
print(linear_search(items, 34))
print(linear_search(items, 45))
print(linear_search(items, 12))
