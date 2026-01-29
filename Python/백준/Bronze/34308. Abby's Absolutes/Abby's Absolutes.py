n,k = map(int,input().split())
w = list(map(int,input().split()))
mid = (n + 1) / 2
for i in w:
  print(n if i > mid else 1, end =" ")