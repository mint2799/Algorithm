for _ in range(int(input())):
  p,m = map(int,input().split())
  seat = [0]*m
  cnt = 0
  for _ in range(p):
    s = int(input())
    if seat[s-1] == 0: seat[s-1]=1
    else: cnt += 1
  print(cnt)