s = input()
suff = sorted([s[i:] for i in range(len(s))])
print(*suff)