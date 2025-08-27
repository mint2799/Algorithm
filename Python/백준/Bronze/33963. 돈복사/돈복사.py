n = int(input())
cnt = 0
curr = len(str(n))
while (len(str(n*2))==curr):
  n *= 2
  cnt += 1
print(cnt)