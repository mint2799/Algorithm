n = int(input())
maxNum = 1
cnt = 1
while n > maxNum:
  maxNum += 6*cnt
  cnt += 1
print(cnt)