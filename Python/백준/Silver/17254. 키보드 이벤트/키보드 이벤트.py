n, m = map(int,input().split())
keys = sorted([input().split() for _ in range(m)], key = lambda x:(int(x[1]),int(x[0]))) 
[print(keys[i][2],end='') for i in range(m)]