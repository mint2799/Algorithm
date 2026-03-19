n, m, k, a, b, c = map(int, input().split())
d = {"Joffrey": a*n, "Robb": b*m, "Stannis": c*k}
print(*sorted([x for x in d if d[x]==max(d.values())]))