nums = []
for _ in range(int(input())):
  n = int(input())
  nums.append(n) if n != 0 else nums.pop()
print(sum(nums))