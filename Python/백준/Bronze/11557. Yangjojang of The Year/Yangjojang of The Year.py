for _ in range(int(input())):
  dict = {}
  for _ in range(int(input())):
    s,l = input().split()
    dict[s] = int(l)
  print(max(dict,key=dict.get))