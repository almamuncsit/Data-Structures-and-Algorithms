class Sort:
    def insertion_sort(self, items):
        for i in range(1, len(items)):
            item = items[i]
            j = i - 1

            while j >= 0 and items[j] > item:
                items[j + 1] = items[j]
                j -= 1

            items[j + 1] = item


items = [190, 20, 310, 450, 60, 110, 121, 270]
sort = Sort()
print('Before sort')
print(items)
sort.insertion_sort(items)
print('After sort')
print(items)
