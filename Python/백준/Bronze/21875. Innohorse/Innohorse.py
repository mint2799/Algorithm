A = input()
B = input()

col_A = ord(A[0]) - ord('a')
row_A = int(A[1]) - 1
col_B = ord(B[0]) - ord('a')
row_B = int(B[1]) - 1

dx = abs(col_A - col_B)
dy = abs(row_A - row_B)
print(*sorted([dx, dy]))