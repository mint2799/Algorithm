team1 = list(map(int, input().split()))
team2 = list(map(int, input().split()))

score1 = sum(team1[i] * (i+1) for i in range(3))
score2 = sum(team2[i] * (i+1) for i in range(3))
print(1 if score1 > score2 else 2 if score2 > score1 else 0)