from typing import List


class Sort:
    def marge_sort(self, items: List[int]):
        if len(items) <= 1:
            return items
        middle = len(items) // 2
        left_arr = self.marge_sort(items[:middle])
        right_arr = self.marge_sort(items[middle:])

        return Sort.marge(left_arr, right_arr)

    @staticmethod
    def marge(left_arr, right_arr):
        temp_arr = []
        while len(left_arr) > 0 and len(right_arr) > 0:
            if left_arr[0] < right_arr[0]:
                temp_arr.append(left_arr.pop(0))
            else:
                temp_arr.append(right_arr.pop(0))

        if len(left_arr) > 0:
            temp_arr += left_arr
        else:
            temp_arr += right_arr
        return temp_arr


items = [109, 20, 301, 405, 60, 101, 121, 207]
sort = Sort()
print('Before Sort')
print(items)
items = sort.marge_sort(items)
print('After Sort')
print(items)
