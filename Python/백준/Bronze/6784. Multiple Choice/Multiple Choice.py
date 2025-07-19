n = int(input())
que = [input() for _ in range(n)]
ans = [input() for _ in range(n)]
print(sum([q==a for q,a in zip(que,ans)]))