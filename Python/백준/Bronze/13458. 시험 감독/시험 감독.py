import math
n = int(input())
a = list(map(int,input().split()))
b,c = map(int,input().split())
print(sum([math.ceil((i-b)/c)+1 if i-b > 0 else 1 for i in a]))