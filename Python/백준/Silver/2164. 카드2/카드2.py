from collections import deque
c = deque(i+1 for i in range(int(input())))
while len(c) > 1:
  c.popleft()
  c.append(c.popleft())
print(*c)