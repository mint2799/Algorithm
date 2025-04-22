for i in range(1,int(input())+1):
  a,b = map(int,input().split())
  I = a // b
  n = a % b
  d = b
  result = f'Case {i}: '
  result = result + (f'{I}' if n == 0 else f'{n}/{d}' if I == 0 else f'{I} {n}/{d}')
  print(result)