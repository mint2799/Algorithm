n,m = map(int,input().split())
q = list(map(int,input().split()))
c = [input().split() for _ in range(m)]
total = {}
for i in c:
  num = i[0]
  a = i[1:]
  score = 0
  for j in range(n):
    if a[j]=='O': score += q[j]
  total[num] = score
print(*min(total.items(), key=lambda x:(-x[1], int(x[0]))))