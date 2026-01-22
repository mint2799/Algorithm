result = ["zilch", "double", "double-double", "triple-double"]
for _ in range(int(input())):
    stats = list(map(int, input().split()))
    cnt = sum(s >= 10 for s in stats)
    print(*stats,result[cnt], "\n")