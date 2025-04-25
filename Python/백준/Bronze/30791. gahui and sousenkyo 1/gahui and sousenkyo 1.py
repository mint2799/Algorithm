rank = list(map(int,input().split()))
cnt = 0
for i in range(1,len(rank)):
  if rank[0]-rank[i] <= 1000:
    cnt += 1
print(cnt)