for _ in range(int(input())):
    n, x, y = map(int, input().split())
    c = list(map(int, input().split()))
    print("BOTH" if (x==c[0] and y==c[-1]) else "EASY" if x==c[0] else "HARD" if y==c[-1] else "OKAY")