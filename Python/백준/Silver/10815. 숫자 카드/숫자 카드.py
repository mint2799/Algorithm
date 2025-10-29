import sys

n = int(sys.stdin.readline())
cd = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
chk = list(map(int, sys.stdin.readline().split()))

for c in chk:
    low, high = 0, n-1
    exist = False
    while low <= high:
        mid = (low + high) // 2
        if cd[mid] > c:
            high = mid - 1
        elif cd[mid] < c:
            low = mid + 1
        else:
            exist = True
            break
    print(1 if exist else 0, end=' ')