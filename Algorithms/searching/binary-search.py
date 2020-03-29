def binary_search(items, val):
    start = 0
    end = len(items) - 1

    while start <= end:
        mid = (start + end) // 2
        if items[mid] == val:
            return mid
        elif val < items[mid]:
            end = mid - 1
        else:
            start = mid + 1

    if start > end:
        return None


# Initialize the sorted list
items = [20, 70, 110, 109, 304, 503, 702, 705]

# Print the search result
print(binary_search(items, 304))
print(binary_search(items, 12))
