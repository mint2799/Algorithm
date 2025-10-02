import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    wear = {}
    for _ in range(n):
        name, type = input().split()
        if type in wear:
            wear[type].append(name)
        else: wear[type] = [name]
    res = 1
    for c in wear.values():
        res *= len(c)+1
    print(res - 1)