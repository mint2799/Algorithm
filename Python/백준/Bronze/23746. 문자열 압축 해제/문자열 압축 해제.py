st = {}; de = ""
for _ in range(int(input())):
  a,b = input().split()
  st[b] = a
for i in input():
  de += st[i]
s,e = map(int,input().split())
print(de[s-1:e])