class Sort:
    def marge_sort(self, items):
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


items = [19, 2, 31, 45, 6, 11, 121, 27]
sort = Sort()
items = sort.marge_sort(items)
print(items)
