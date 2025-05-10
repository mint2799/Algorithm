for _ in range(int(input())):
  a,b,c,d = map(int,input().split())
  total = b+c+d
  res = 'PASS' if (total>=55 and b>=10.5 and c>=7.5 and d>=12) else 'FAIL'
  print(f'{a} {total} {res}')