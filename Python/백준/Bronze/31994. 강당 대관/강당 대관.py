s = [list(input().split()) for _ in range(7)]
print(max(s, key=lambda x: int(x[1]))[0])