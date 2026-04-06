h, w = map(int, input().split())
s = ''.join(input().strip() for _ in range(h))
print(min(s.count('0'), s.count('1')))