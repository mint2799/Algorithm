import sys
input = sys.stdin.readline
n = int(input())
x = list(map(int,input().split()))
rank = {v:i for i, v in enumerate(sorted(set(x)))}
print(*[rank[v] for v in x])