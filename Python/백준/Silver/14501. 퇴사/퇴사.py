n = int(input())
t = [0] * (n+1)
p = [0] * (n+1)
for i in range(1,n+1):
  t[i],p[i] = map(int,input().split())
dp = [0] * (n+2)
max_p = 0
for i in range(n+1):
  max_p = max(max_p,dp[i])
  if i+t[i] <= n+1:
    dp[i+t[i]] = max(dp[t[i]+i], p[i]+max_p)
print(max(dp))