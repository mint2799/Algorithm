coor = [list(map(int,input().split())) for _ in range(int(input()))]
x,y = zip(*coor)
l = max(max(x)-min(x), max(y)-min(y))
print(l*l)