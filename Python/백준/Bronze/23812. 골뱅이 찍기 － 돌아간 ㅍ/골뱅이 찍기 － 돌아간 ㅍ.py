n = int(input())
for i in range(5*n):
  if((n<=i<2*n) or (3*n<=i<4*n)):
    print('@'*(5*n))
  else: print('@'*n+' '*(3*n)+'@'*n)