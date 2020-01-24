class Sort:
	def bubblesort(self, list):
		for n in range(len(list)-1, 0, -1):
			for i in range(0, n):
				if list[i] > list[i+1]:
					list[i+1], list[i] = list[i], list[i+1]	


list = [19,2,31,45,6,11,121,27]
sort = Sort()
sort.bubblesort(list)
print(list)