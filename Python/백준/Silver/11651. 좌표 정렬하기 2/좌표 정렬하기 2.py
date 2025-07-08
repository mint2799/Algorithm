coord = sorted([list(map(int,input().split())) for _ in range(int(input()))], key=lambda x:(x[1],x[0]))
print('\n'.join(f"{x} {y}" for x, y in coord))