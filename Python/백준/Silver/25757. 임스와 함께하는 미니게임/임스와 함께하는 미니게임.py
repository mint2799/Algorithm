n, game = input().split()
player = len(set([input() for _ in range(int(n))]))
print(player if game=="Y" else player//2 if game=="F" else player//3)