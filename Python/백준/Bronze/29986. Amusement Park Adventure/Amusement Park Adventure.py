p,h = map(int,input().split())
l = list(map(int,input().split()))
cnt = 0
for i in l:
    if h >= i:
        cnt += 1
print(cnt)