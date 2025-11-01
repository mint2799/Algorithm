def Queens(i):
    if i == n:
        global cnt
        cnt += 1
        return
    for j in range(n):
        if not col_used[j] and not diag1[i + j] and not diag2[i - j + n - 1]:
            col_used[j] = diag1[i + j] = diag2[i - j + n - 1] = True
            Queens(i + 1)
            col_used[j] = diag1[i + j] = diag2[i - j + n - 1] = False
n = int(input())
cnt = 0
col_used = [False] * n
diag1 = [False] * (2 * n - 1)
diag2 = [False] * (2 * n - 1)
Queens(0)
print(cnt)