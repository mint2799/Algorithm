import sys
read = sys.stdin.readline
coord = [list(map(int,read().split())) for _ in range(int(read()))]
max_d = 0
for i in range(len(coord)-1):
  for j in range(i+1, len(coord)):
    d = (coord[j][0]-coord[i][0])**2 + (coord[j][1]-coord[i][1])**2
    if d>max_d:
      cow1, cow2 = i+1, j+1
      max_d = d
print(cow1, cow2)