players = sorted([list(map(int,input().split())) for _ in range(int(input()))], key = lambda x: (x[1]*x[2]*x[3], x[1]+x[2]+x[3], x[0]))
print(" ".join(str(players[i][0]) for i in range(3)))