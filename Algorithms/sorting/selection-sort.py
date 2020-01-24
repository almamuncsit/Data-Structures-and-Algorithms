class Sort:
	def selectionSort(self, list):
		for i in range(len(list)):
			for j in range(i+1, len(list)):
				if list[i] > list[j]:
					list[i], list[j] = list[j], list[i]


	def selectionSort2(self, list):
		for i in range(len(list)):
			min = i
			for j in range(i+1, len(list)):
				if list[min] > list[j]:
					min = j
			if min > i:
				list[i], list[min] = list[min], list[i]


list = [19,2,31,45,6,11,121,27]
sort = Sort()
sort.selectionSort2(list)
print(list)