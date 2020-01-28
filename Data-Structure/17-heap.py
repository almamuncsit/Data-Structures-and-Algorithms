import heapq

heap = [21,1,45,78,3,5]
heapq.heapify(heap)
print(heap)

# Insert into heap
heapq.heappush(heap, 8)
print(heap)

# Remove element form heap
heapq.heappop(heap)
heapq.heappop(heap)
heapq.heappop(heap)
heapq.heappop(heap)
print(heap)
heapq.heapreplace(heap, 150)
print(heap)