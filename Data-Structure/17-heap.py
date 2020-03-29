import heapq

min_heap = [21, 1, 45, 78, 3, 5]
heapq.heapify(min_heap)
print(min_heap)

# Insert into min_heap
heapq.heappush(min_heap, 8)
print(min_heap)

# Remove element form min_heap
heapq.heappop(min_heap)
heapq.heappop(min_heap)
heapq.heappop(min_heap)
heapq.heappop(min_heap)
print(min_heap)
heapq.heapreplace(min_heap, 150)
print(min_heap)
