while 1:
    n = int(input())
    if n == 0: break
    a = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        current = a[i]
        if i >= 1:
            current += a[i-1]
        if i >= 2:
            current += a[i-2]
        ans = max(ans, current)
    print(ans)