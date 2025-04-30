for _ in range(int(input())):
  c,p = map(int,input().split())
  print(c,p)
  if c>1:
    p += (p-2)*(c-1)
  print(p)