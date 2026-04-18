dir = 0

for _ in range(10):
    t = int(input())
    if t == 1: dir = (dir + 1) % 4
    elif t == 2: dir = (dir + 2) % 4
    elif t == 3: dir = (dir + 3) % 4
dirs = ['N', 'E', 'S', 'W']
print(dirs[dir])