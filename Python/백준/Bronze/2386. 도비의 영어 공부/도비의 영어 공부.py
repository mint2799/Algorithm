while 1:
  a,*s = input().split()
  if a == '#': break
  cnt = 0
  for i in s:
    i = i.lower()
    cnt += i.count(a)
  print(f'{a} {cnt}')