n = int(input())
coded = input().split()
decoded = coded[0][0]
for i in range(1,n):
  prev = len(coded[i-1])
  curr = coded[i]
  decoded = decoded + (curr[prev-1] if prev <= len(curr) else ' ')
print(decoded)