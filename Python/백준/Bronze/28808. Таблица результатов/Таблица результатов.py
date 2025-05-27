cnt = 0
n,m = map(int,input().split())
for _ in range(n):
  if "+" in input():
    cnt+=1
print(cnt)