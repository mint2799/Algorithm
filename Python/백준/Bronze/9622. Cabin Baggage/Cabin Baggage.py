cnt = 0
for _ in range(int(input())):
    l, w, d, W = map(float, input().split())
    ok = ((l <= 56 and w <= 45 and d <= 25) or (l + w + d <= 125)) and W <= 7
    print(int(ok))
    cnt += ok
print(cnt)