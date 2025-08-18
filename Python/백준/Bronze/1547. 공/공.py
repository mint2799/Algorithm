xy = [list(map(int,input().split())) for _ in range(int(input()))]
cup = [1,2,3]
for x, y in xy:
    ix = cup.index(x)
    iy = cup.index(y)
    cup[ix], cup[iy] = cup[iy], cup[ix]
print(cup[0])