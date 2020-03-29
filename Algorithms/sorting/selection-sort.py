from typing import List


class Sort:
    def selection_sort(self, items: List[int]):
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                if items[i] > items[j]:
                    items[i], items[j] = items[j], items[i]

    def selection_sort_another(self, items: List[int]):
        for i in range(len(items)):
            min_index = i
            for j in range(i + 1, len(items)):
                if items[min_index] > items[j]:
                    min_index = j
            if min_index > i:
                items[i], items[min_index] = items[min_index], items[i]


items = [190, 20, 310, 450, 60, 110, 121, 270]
sort = Sort()

print('Before Sort')
print(items)
sort.selection_sort_another(items)
print('After Sort')
print(items)
