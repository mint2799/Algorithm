while 1:
  n = int(input())
  if n == 0: break
  stud = [input().split() for _ in range(n)]
  max_height = max(stud, key=lambda x: x[1])
  res = [name for name,h in stud if h == max_height[1]]
  print(*res)