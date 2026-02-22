q = [int(input()) for _ in range(int(input()))]
print('ez' if q.index(min(q)) == 0 else 'hard' if q.index(max(q)) == 0 else '?')