d, p = 0, 0
for _ in range(int(input())):
  if input() == "D": d+=1
  else: p+=1
  if abs(d-p) == 2: break
print(f'{d}:{p}')