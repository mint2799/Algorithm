t,x = map(int,input().split())
attd = 1
for _ in range(int(input())):
  k = int(input())
  a = list(map(int,input().split()))
  if x not in a:
    attd = 0
print("YES" if attd else "NO")