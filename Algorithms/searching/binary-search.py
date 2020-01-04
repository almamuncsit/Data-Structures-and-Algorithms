
def bsearch(items, val):
	start = 0
	end = len(items) - 1

	while start <= end:
		mid = (start + end)//2
		if items[mid] == val:
			return mid
		elif val < items[mid]:
			end = mid - 1
		else:
			start = mid + 1
	
	if start > end:
		return None
	

# Initialize the sorted list
items = [2,7,11,19,34,53,72,75]

# Print the search result
print(bsearch(items,34))
print(bsearch(items, 12))