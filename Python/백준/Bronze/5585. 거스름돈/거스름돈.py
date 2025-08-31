m = 1000-int(input())
res = 0
for c  in [500,100,50,10,5,1]:
    res += m//c
    m %= c
print(res)