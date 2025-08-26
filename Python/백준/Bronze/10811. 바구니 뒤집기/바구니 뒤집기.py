n,m = map(int,input().split())
bk = [i+1 for i in range(n)]
rvs = [list(map(int,input().split())) for _ in range(m)]
for i,j in rvs:
  bk[i-1:j] = reversed(bk[i-1:j])
print(*bk)