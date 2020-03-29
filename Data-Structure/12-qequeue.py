import collections

double_ended_queue = collections.deque(["Mon", "Tue", "Wed"])

double_ended_queue.append("Thu")

print("Appended at right - ")
print(double_ended_queue)

double_ended_queue.appendleft("Sun")

print("Appended at right at left is - ")
print(double_ended_queue)

double_ended_queue.pop()

print("Deleting from right - ")
print(double_ended_queue)

double_ended_queue.popleft()

print("Deleting from left - ")
print(double_ended_queue)
