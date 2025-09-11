a = [int(input()) for _ in range(3)]
b = [int(input()) for _ in range(3)]
A = a[0]*3+a[1]*2+a[2]
B = b[0]*3+b[1]*2+b[2]
print('A' if A>B else 'B' if B>A else 'T')