class Sort:
    def bubblesort(self, items):
        for n in range(len(items) - 1, 0, -1):
            for i in range(0, n):
                if items[i] > items[i + 1]:
                    items[i + 1], items[i] = items[i], items[i + 1]


items = [190, 20, 310, 450, 60, 110, 121, 270]
sort = Sort()
print('Before Sort')
print(items)
sort.bubblesort(items)
print('After Sort')
print(items)
