n, a = map(int, input().split())
print(sum(x // a for x in map(int, input().split())))