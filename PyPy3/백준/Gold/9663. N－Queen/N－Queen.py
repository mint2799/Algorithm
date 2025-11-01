def Queens(i):
    if promising(i):
        if i == n:
            global cnt
            cnt += 1
        else:
            for j in range(1, n + 1):
                col[i + 1] = j
                Queens(i + 1)
def promising(i):
    for k in range(1, i):
        if col[k] == col[i] or abs(col[i] - col[k]) == i - k:
            return False
    return True
n = int(input())
cnt = 0
col = [0] * (n + 1)
Queens(0)
print(cnt)