from collections import deque

queue = deque(['one', 'two', 'three', 'four'])
queue.append('five')
queue.append('six')
queue.popleft()
queue.popleft()
print(queue)
