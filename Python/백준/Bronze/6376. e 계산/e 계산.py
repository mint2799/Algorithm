import math
def cal(n):
  e = sum([1 / math.factorial(i) for i in range(n+1)])
  return e
print("n e")
print("- -----------")
print("0 1\n1 2\n2 2.5")
for i in range(3,10):
  print(f'{i} {cal(i):.9f}')