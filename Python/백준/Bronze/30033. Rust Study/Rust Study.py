n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(sum(j >= i for i,j in zip(a,b)))