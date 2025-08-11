s = sum(sorted([int(input()) for _ in range(4)], reverse=True)[:3])
h = max([int(input()) for _ in range(2)])
print(s+h)