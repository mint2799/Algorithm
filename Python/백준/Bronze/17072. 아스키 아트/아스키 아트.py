n, m = map(int, input().split())

def intensity(r, g, b):
    return 2126*r + 7152*g + 722*b

for _ in range(n):
    pixels = list(map(int, input().split()))
    for j in range(m):
        r, g, b = pixels[3*j], pixels[3*j+1], pixels[3*j+2]
        res = intensity(r, g, b)
        if res < 510000:
            print('#', end='')
        elif res < 1020000:
            print('o', end='')
        elif res < 1530000:
            print('+', end='')
        elif res < 2040000:
            print('-', end='')
        else:
            print('.', end='')
    print()