for _ in range(int(input())):
  d,n,s,p = map(int,input().split())
  print("do not parallelize" if n*s < d+n*p else "parallelize" if n*s > d+n*p else "does not matter")