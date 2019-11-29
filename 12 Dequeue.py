import collections

DoubleEnded = collections.deque(["Mon","Tue","Wed"])

DoubleEnded.append("Thu")

print ("Appended at right - ")
print (DoubleEnded)

DoubleEnded.appendleft("Sun")

print ("Appended at right at left is - ")
print (DoubleEnded)

DoubleEnded.pop()

print ("Deleting from right - ")
print (DoubleEnded)

DoubleEnded.popleft()

print ("Deleting from left - ")
print (DoubleEnded)