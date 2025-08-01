n = int(input())
bat = list(map(int,input().split()))
s = 0
for i in bat:
  if i == -1: n -= 1
  else: s += i
print(s/n)