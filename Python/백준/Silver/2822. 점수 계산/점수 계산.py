score = [int(input()) for _ in range(8)]
q = sorted(score,reverse=True)[:5]
idx = [score.index(i)+1 for i in q]
print(sum(q), *sorted(idx))