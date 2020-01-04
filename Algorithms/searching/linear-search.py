

def lsearch(items, val):
	length = len(items)
	for i in range(0, length):
		if items[i] == val:
			return i
	
	return None
	

# Initialize the sorted list
items = [2,7,11,19,34,53,3,45,72,75]

# Print the search result
print(lsearch(items,34))
print(lsearch(items,45))
print(lsearch(items, 12))