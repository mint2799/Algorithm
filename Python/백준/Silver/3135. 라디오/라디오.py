a,b = map(int,input().split())
hz = min([abs(b-int(input())) for _ in range(int(input()))])
cnt = 1
if abs(a-b) <= hz:
  cnt = abs(a-b)
else: cnt += hz
print(cnt)