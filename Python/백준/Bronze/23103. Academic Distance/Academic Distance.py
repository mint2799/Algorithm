n = int(input())
coords = [list(map(int,input().split())) for _ in range(n)]
total = 0
for i in range(n-1):
  dx = abs(coords[i+1][0]-coords[i][0])
  dy = abs(coords[i+1][1]-coords[i][1])
  total += dx+dy
print(total)