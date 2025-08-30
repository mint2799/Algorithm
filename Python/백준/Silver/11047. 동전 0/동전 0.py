n,k = map(int,input().split())
a = sorted([int(input()) for _ in range(n)], reverse=True)
res = 0
for i in a:
    if k >= i:
        res += k//i
        k %= i
        if k <= 0: break
print(res)