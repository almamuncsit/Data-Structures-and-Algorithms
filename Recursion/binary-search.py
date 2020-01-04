
def bsearch(items, val, start, end):
	if start > end:
		return None
	
	mid = start + ((end - start)//2)
	if items[mid] == val:
		return mid
	elif val < items[mid]:
		return bsearch(items, val, start, mid-1)
	else:
		return bsearch(items, val, mid+1, end)
	

# Initialize the sorted list
items = [2,7,11,19,34,53,72,75]

# Print the search result
end = len(items) - 1
print(bsearch(items, 34, 0, end))
print(bsearch(items, 12, 0, end))