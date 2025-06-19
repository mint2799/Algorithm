res = {1:'A', 2:'B', 3:'C', 4:'D', 0:'E'}
for _ in range(3):
  yut = list(map(int,input().split()))
  print(res[yut.count(0)])