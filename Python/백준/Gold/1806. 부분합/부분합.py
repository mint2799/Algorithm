def twoPointer(arr, target):
  left = 0
  curr_sum = 0
  min_len = float('inf')
  for right in range(len(arr)):
    curr_sum += arr[right]
    while curr_sum >= target and left <= right:
      min_len = min(min_len, right - left + 1)
      curr_sum -= arr[left]
      left += 1
  return min_len if min_len != float('inf') else 0
n, s = map(int,input().split())
seq = list(map(int,input().split()))
print(twoPointer(seq,s))