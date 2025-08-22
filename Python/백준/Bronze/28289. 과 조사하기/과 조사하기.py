p = int(input())
std = [list(map(int,input().split())) for _ in range(p)]
s = e = a = f = 0
for x,y,_ in std:
  if x == 1:
    f += 1
  elif y in (1,2):
    s += 1
  elif y == 3:
    e += 1
  elif y == 4:
    a += 1
print(s,e,a,f)