n = int(input())
cnt = 0
for _ in range(3):
  wheel = list(map(int,input().split()))
  if 7 in wheel: cnt += 1
print("777" if cnt==3 else 0)