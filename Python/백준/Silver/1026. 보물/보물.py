n = int(input())
a = sorted(list(map(int,input().split())), reverse=True)
b = sorted(list(map(int,input().split())))
print(sum(x*y for x,y in zip(a,b)))