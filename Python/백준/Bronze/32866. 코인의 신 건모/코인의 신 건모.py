n = int(input())
x = int(input())
curr = n*(1-x/100)
print(f'{(n/curr-1)*100:.6f}')