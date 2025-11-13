n, k = map(int,input().split())
p = [0]*(k+1)
for i in range(n):
    w, v = map(int,input().split())
    for j in range(k, w-1, -1):
        p[j] = max(p[j], p[j-w] + v)
print(p[k])