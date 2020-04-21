class MinHeap:
    def __init__(self, items=[]):
        self.heap = [0]
        for item in items:
            self.push(item)

    def push(self, item):
        self.heap.append(item)
        self.__float_up(self.size() - 1)

    def peak(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if self.size() < 2:
            return False
        if self.size() == 2:
            return self.heap.pop()

        self.__swap(1, self.size() - 1)
        item = self.heap.pop()
        self.__max_heapify(1)

        return item

    def __swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def __float_up(self, index):
        parent = index // 2
        if parent < 1:
            return
        elif self.heap[index] < self.heap[parent]:
            self.__swap(index, parent)
            self.__float_up(parent)

    def __max_heapify(self, index):
        smallest_idx = index
        left = index * 2
        right = left + 1
        if self.size() > left and self.heap[left] < self.heap[smallest_idx]:
            smallest_idx = left
        if self.size() > right and self.heap[right] < self.heap[smallest_idx]:
            smallest_idx = right
        if smallest_idx != index:
            self.__swap(index, smallest_idx)
            self.__max_heapify(smallest_idx)

    def size(self):
        return len(self.heap)

    def delete(self, item):
        for i in range(1, self.size()):
            if self.heap[i] == item:
                self.__swap(i, self.size() - 1)
                self.heap.pop()
                self.__max_heapify(i)
                return


if __name__ == '__main__':
    items = [12, 7, 1, 3, 10, 17, 19, 2, 5]
    heap = MinHeap(items)
    print(heap.heap[1:])
    heap.delete(10)
    print(heap.heap[1:])
    # print(heap.peak())
    # while heap.size() > 1:
    #     print(heap.pop())

