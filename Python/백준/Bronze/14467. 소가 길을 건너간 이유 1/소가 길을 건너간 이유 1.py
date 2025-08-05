obs = [list(map(int,input().split())) for _ in range(int(input()))]
cows = {}; cnt = 0
for num, pos in obs:
  if num in cows and cows[num] ^ pos:
    cnt += 1
  cows[num] = pos
print(cnt)