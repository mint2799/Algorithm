balloons = [input() for _ in range(int(input()))]
for i in balloons:
  print(min(i.count('a'),i.count('b')))