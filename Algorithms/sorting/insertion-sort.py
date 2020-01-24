class Sort:
	def insertionSort(self, list):
		for i in range(1, len(list)):
			item = list[i]
			j = i-1
			
			while j >= 0 and list[j] > item:
				list[j+1] = list[j]
				j -= 1
			
			list[j+1] = item



list = [19,2,31,45,6,11,121,27]
sort = Sort()
sort.insertionSort(list)
print(list)