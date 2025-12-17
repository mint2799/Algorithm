res = 0
for _ in range(int(input())):
    c,k = map(int,input().split())
    res += c*k
print(res)