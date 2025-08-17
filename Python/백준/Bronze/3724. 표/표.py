for _ in range(int(input())):
  m,n = map(int,input().split())
  grid = [list(map(int,input().split())) for _ in range(n)]
  col = -1
  res = None
  for j in range(m):
    prod = 1
    for i in range(n):
      prod *= grid[i][j]
    if res is None or prod > res or (prod == res and j > col):
      res = prod
      col = j
  print(col+1)