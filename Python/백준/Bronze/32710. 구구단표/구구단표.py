n = int(input())
check = 0
for i in range(1,10):
  if n%i==0 and n//i<=9:
    check = 1
    break
print(check)