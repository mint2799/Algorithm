a, b = map(int,input().split())
x = max(a, b); y = min(a, b)
print(x-y-1 if x!=y else 0)
for i in range(y+1,x):
    print(i, end=' ')