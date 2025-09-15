while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    n = s[0]
    nums = s[1:]
    res = [nums[0]]
    for i in range(1, n):
        if nums[i] != nums[i-1]:
            res.append(nums[i])
    print(*res, '$')