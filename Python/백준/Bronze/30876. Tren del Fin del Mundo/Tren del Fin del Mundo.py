N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]
answer = min(points, key=lambda p: p[1])
print(answer[0], answer[1])