from collections import deque
n = int(input())
q = deque([i for i in range(1, n+1)])
res = []
while len(q) > 1:
    res.append(q.popleft())
    q.append(q.popleft())
print(*res, q.popleft())